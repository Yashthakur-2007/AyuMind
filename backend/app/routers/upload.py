
from pathlib import Path

from fastapi import APIRouter, UploadFile, File

from app.services.upload_service import save_uploaded_file
from app.services.pdf_parser_service import parse_pdf
from app.services.text_cleaning_service import clean_text
from app.services.chunking_service import chunk_text
from app.services.embedding_service import generate_embeddings
from app.services.vector_store_service import store_chunks

router = APIRouter()


@router.post("/upload")
def upload_file(file: UploadFile = File(...)):

    # 1. Save uploaded PDF
    file_path = save_uploaded_file(file)

    # 2. Generate document ID
    document_id = Path(file_path).stem

    # 3. Extract PDF text
    extracted_text = parse_pdf(file_path)

    # 4. Clean extracted text
    cleaned_text = clean_text(extracted_text)

    # 5. Generate chunks
    chunks = chunk_text(cleaned_text)

    # 6. Generate embeddings
    embeddings = generate_embeddings(chunks)

    # 7. Store chunks and embeddings in ChromaDB
    store_chunks(document_id, chunks, embeddings)

    return {
        "message": "File uploaded and processed successfully",
        "document_id": document_id,
        "filename": file.filename,
        "text": extracted_text,
        "cleaned_text": cleaned_text,
        "chunks": chunks,
        "total_chunks": len(chunks),
        "stored_in_vector_db": True
    }
