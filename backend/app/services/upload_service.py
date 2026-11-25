
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile, HTTPException


# Upload directory
BASE_DIR = Path(__file__).resolve().parents[1]
UPLOAD_DIR = BASE_DIR / "storage" / "uploads"

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


def save_uploaded_file(file: UploadFile) -> str:

    # Validate filename
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is missing."
        )

    # Validate extension
    if Path(file.filename).suffix.lower() != ".pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Validate content type
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Invalid file content type."
        )

    # Read file and validate size
    file_content = file.file.read(MAX_FILE_SIZE + 1)

    if len(file_content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File size exceeds the 10 MB limit."
        )

    # Validate PDF signature
    if not file_content.startswith(b"%PDF-"):
        raise HTTPException(
            status_code=400,
            detail="Invalid PDF file signature."
        )

    # Create upload directory
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    # Generate unique filename
    safe_filename = Path(file.filename).name
    unique_filename = f"{uuid4().hex}_{safe_filename}"

    file_path = UPLOAD_DIR / unique_filename

    # Save file
    with open(file_path, "wb") as buffer:
        buffer.write(file_content)

    return str(file_path)