
import fitz
from fastapi import HTTPException


def parse_pdf(file_path: str):
    try:
        document = fitz.open(file_path)

        if document.is_encrypted:
            document.close()
            raise HTTPException(
                status_code=400,
                detail="Password-protected PDFs are not supported."
            )

        pages = []

        for page in document:
            pages.append(page.get_text())

        document.close()

        return "\n".join(pages)

    except HTTPException:
        raise

    except fitz.FileDataError:
        raise HTTPException(
            status_code=400,
            detail="Invalid or corrupted PDF file."
        )

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to read PDF file."
        )
