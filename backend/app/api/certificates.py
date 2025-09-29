from fastapi import APIRouter
from app.services.generator import generate_certificate

router = APIRouter()

@router.post("/generate")
def create_certificate(name: str, track: str):
    path = generate_certificate(name, track)
    return {"message": "Certificate generated", "path": path}
