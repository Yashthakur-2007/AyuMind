def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200):
    """
    Split text into overlapping chunks.

    Args:
        text: Extracted document text.
        chunk_size: Maximum number of characters in each chunk.
        overlap: Number of characters shared between consecutive chunks.

    Returns:
        A list of text chunks.
    """

    if not text:
        return []

    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than 0.")

    if overlap < 0:
        raise ValueError("Overlap cannot be negative.")

    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size.")

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size

        chunk = text[start:end]
        chunks.append(chunk)

        start = end - overlap

    return chunks