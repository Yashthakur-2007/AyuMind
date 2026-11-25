
from sentence_transformers import SentenceTransformer

# Load the model once when the service is initialized
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def generate_embeddings(chunks: list[str]) -> list[list[float]]:
    """
    Convert text chunks into numerical embeddings.
    """
    if not chunks:
        return []

    embeddings = model.encode(chunks)

    return embeddings.tolist()
