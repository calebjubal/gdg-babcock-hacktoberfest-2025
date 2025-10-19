from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from ..models.certificates import CertificateCreate, CertificateResponse, Certificate
from ..services.generator import generate_certificate
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
