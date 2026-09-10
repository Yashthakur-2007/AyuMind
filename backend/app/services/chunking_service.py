import re


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200):
    """
    Split cleaned text into overlapping chunks.

    The function tries to preserve paragraphs and sentences
    instead of cutting text at an arbitrary character position.
    """

    if not text:
        return []

    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than 0.")

    if overlap < 0:
        raise ValueError("Overlap cannot be negative.")

    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size.")

    # Split text into paragraphs
    paragraphs = [
        paragraph.strip()
        for paragraph in re.split(r"\n\s*\n", text)
        if paragraph.strip()
    ]

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:

        # Add paragraph if it fits inside current chunk
        if len(current_chunk) + len(paragraph) + 1 <= chunk_size:

            if current_chunk:
                current_chunk += "\n\n"

            current_chunk += paragraph

        else:

            # Save current chunk
            if current_chunk:
                chunks.append(current_chunk)

            # If paragraph is too large, split it by sentences
            if len(paragraph) > chunk_size:

                sentences = re.split(
                    r"(?<=[.!?])\s+",
                    paragraph
                )

                current_chunk = ""

                for sentence in sentences:

                    if len(current_chunk) + len(sentence) + 1 <= chunk_size:

                        if current_chunk:
                            current_chunk += " "

                        current_chunk += sentence

                    else:

                        if current_chunk:
                            chunks.append(current_chunk)

                        current_chunk = sentence

            else:
                current_chunk = paragraph

    # Add final chunk
    if current_chunk:
        chunks.append(current_chunk)

    # Add sentence-based overlap
    final_chunks = []

    for i, chunk in enumerate(chunks):

        if i == 0:
            final_chunks.append(chunk)
            continue

        previous_chunk = chunks[i - 1]

        sentences = re.split(
            r"(?<=[.!?])\s+",
            previous_chunk
        )

        overlap_sentences = []
        overlap_length = 0

        for sentence in reversed(sentences):

            if overlap_length + len(sentence) > overlap:
                break

            overlap_sentences.insert(0, sentence)
            overlap_length += len(sentence)

        overlap_text = " ".join(overlap_sentences)

        if overlap_text:
            final_chunks.append(
                overlap_text + "\n" + chunk
            )
        else:
            final_chunks.append(chunk)

    return final_chunks