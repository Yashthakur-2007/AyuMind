from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import save_uploaded_file
from app.schemas.parser_schema import ParseRequest
from app.services.pdf_parser_service import parse_pdf

router = APIRouter()

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    file_path = save_uploaded_file(file)

    extracted_text = parse_pdf(file_path)

    return {
    "message": "File uploaded successfully",
    "filename": file.filename,
    "text": extracted_text
}