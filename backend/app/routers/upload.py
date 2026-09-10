<<<<<<< HEAD

=======
>>>>>>> main
from app.services.text_cleaning_service import clean_text
from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import save_uploaded_file
from app.schemas.parser_schema import ParseRequest
from app.services.pdf_parser_service import parse_pdf
from app.services.chunking_service import chunk_text
router = APIRouter()

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    file_path = save_uploaded_file(file)

    extracted_text = parse_pdf(file_path)
<<<<<<< HEAD
    cleaned_text = clean_text(extracted_text)
=======

    cleaned_text = clean_text(extracted_text)

>>>>>>> main
    chunks = chunk_text(cleaned_text)

    return {
    "message": "File uploaded successfully",
    "filename": file.filename,
    "text": extracted_text,
    "cleaned_text": cleaned_text,
<<<<<<< HEAD
    "Chunks": chunks,
}
=======
    "chunks": chunks,
}
>>>>>>> main
