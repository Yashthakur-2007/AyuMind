
import pymupdf


def parse_pdf(file_path: str) -> str:
    """
    Extract text from all pages of a PDF.
    """

    extracted_pages = []

    with pymupdf.open(file_path) as pdf:
        for page in pdf:
            page_text = page.get_text()
            extracted_pages.append(page_text)

    return "\n".join(extracted_pages)
