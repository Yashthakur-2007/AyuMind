from fastapi import UploadFile, HTTPException
import shutil
import os
import uuid

UPLOAD_FOLDER = "app/storage/uploads"


def save_uploaded_file(file: UploadFile):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
    )

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Invalid PDF content type."
    )

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    unique_id = str(uuid.uuid4())
    unique_filename = f"{unique_id}_{file.filename}"

    file_path = os.path.join(UPLOAD_FOLDER, unique_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path