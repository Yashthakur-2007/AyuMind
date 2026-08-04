from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import save_uploaded_file

router = APIRouter()

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    save_uploaded_file(file)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }