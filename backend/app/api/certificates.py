from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from ..models.certificates import (
    CertificateCreate, 
    CertificateResponse, 
    Certificate,
    BulkCertificateRequest,
    BulkCertificateResponse
)
from ..services.generator import generate_certificate
from ..services.bulk_generator import (
    process_csv_content, 
    generate_bulk_certificates, 
    create_certificates_zip
)
import os
import logging

# Logger setup
logger = logging.getLogger(__name__)

router = APIRouter()

# In-memory store for demo; use DB in production
certificates = {}


@router.post("/", response_model=CertificateResponse)
async def create_certificate(cert: CertificateCreate):
    try:
        # Input validation
        if not cert.participant_name.strip() or not cert.event_name.strip():
            raise HTTPException(
                status_code=400,
                detail="Participant name and event name cannot be empty."
            )

        # Create certificate object
        cert_obj = Certificate(
            participant_name=cert.participant_name,
            event_name=cert.event_name,
            date_issued=cert.date_issued
        )

        output_dir = "certificates"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, cert_obj.filename)

        # Attempt generation
        try:
            generate_certificate(
                cert_obj.participant_name,
                cert_obj.event_name,
                cert_obj.date_issued,
                output_path
            )
        except FileNotFoundError as e:
            logger.error(f"Template file missing: {e}")
            raise HTTPException(status_code=500, detail="Certificate template not found on server.")
        except PermissionError as e:
            logger.error(f"Permission error writing file: {e}")
            raise HTTPException(status_code=500, detail="Server permission error while saving certificate.")
        except Exception as e:
            logger.error(f"Unexpected error during certificate generation: {e}")
            raise HTTPException(status_code=500, detail="Unexpected error during certificate generation.")

        # Save in-memory record
        certificates[cert_obj.unique_id] = {
            "data": cert_obj.to_dict(),
            "file": output_path
        }

        # Successful response
        return CertificateResponse(
            participant_name=cert_obj.participant_name,
            event_name=cert_obj.event_name,
            date_issued=cert_obj.date_issued,
            unique_id=cert_obj.unique_id,
            filename=cert_obj.filename,
            download_url=f"/certificates/{cert_obj.unique_id}",
            created_at=cert_obj.created_at
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unhandled error in POST /certificates: {e}")
        raise HTTPException(status_code=500, detail="Internal server error while creating certificate.")


@router.get("/{unique_id}")
async def get_certificate(unique_id: str):
    try:
        cert_info = certificates.get(unique_id)
        if not cert_info:
            raise HTTPException(status_code=404, detail="Certificate record not found.")

        file_path = cert_info["file"]
        if not os.path.exists(file_path):
            logger.warning(f"File not found for certificate {unique_id}: {file_path}")
            raise HTTPException(status_code=404, detail="Certificate file missing on server.")

        return FileResponse(
            path=file_path,
            filename=os.path.basename(file_path),
            media_type="image/png"
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unhandled error in GET /certificates/{unique_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error while fetching certificate.")


@router.post("/bulk", response_model=BulkCertificateResponse)
async def create_bulk_certificates(request: BulkCertificateRequest):
    """
    Generate certificates for multiple participants
    """
    try:
        output_dir = "certificates/bulk"
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate bulk certificates
        result = generate_bulk_certificates(
            event_name=request.event_name,
            date_issued=request.date_issued,
            participants=request.participants,
            output_dir=output_dir
        )
        
        download_url = None
        if result["successful_certificates"]:
            # Create ZIP file for download
            zip_path = create_certificates_zip(
                result["successful_certificates"], 
                output_dir
            )
            download_url = f"/certificates/bulk/download/{os.path.basename(zip_path)}"
        
        return BulkCertificateResponse(
            success_count=result["success_count"],
            failed_count=result["failed_count"],
            total_count=result["total_count"],
            successful_certificates=result["successful_certificates"],
            failed_certificates=result["failed_certificates"],
            download_url=download_url
        )
        
    except Exception as e:
        logger.error(f"Error in bulk certificate generation: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate bulk certificates: {str(e)}")


@router.post("/bulk/csv", response_model=BulkCertificateResponse)
async def create_bulk_certificates_from_csv(
    event_name: str,
    date_issued: str,
    csv_file: UploadFile = File(...)
):
    """
    Generate certificates from CSV file upload
    CSV should have columns: participant_name, email (optional)
    """
    try:
        # Validate file type
        if not csv_file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="File must be a CSV file")
        
        # Read CSV content
        csv_content = await csv_file.read()
        csv_text = csv_content.decode('utf-8')
        
        # Process CSV and extract participants
        participants = process_csv_content(csv_text)
        
        if not participants:
            raise HTTPException(
                status_code=400, 
                detail="No valid participants found in CSV file"
            )
        
        # Create bulk request
        bulk_request = BulkCertificateRequest(
            event_name=event_name,
            date_issued=date_issued,
            participants=participants
        )
        
        # Generate certificates
        return await create_bulk_certificates(bulk_request)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to process CSV file: {str(e)}")


@router.get("/bulk/download/{filename}")
async def download_bulk_certificates(filename: str):
    """
    Download ZIP file containing bulk certificates
    """
    try:
        file_path = os.path.join("certificates/bulk", filename)
        
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="Bulk certificate file not found")
        
        return FileResponse(
            path=file_path,
            filename=filename,
            media_type="application/zip"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error downloading bulk certificates: {e}")
        raise HTTPException(status_code=500, detail="Failed to download bulk certificates")
