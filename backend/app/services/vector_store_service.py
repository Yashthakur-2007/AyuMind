
from pathlib import Path
import chromadb


# Persistent database location
BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "storage" / "chroma_db"

# Initialize ChromaDB
client = chromadb.PersistentClient(path=str(DB_PATH))

# Create or access our collection
collection = client.get_or_create_collection(
    name="clinical_documents",
    metadata={"hnsw:space": "cosine"}
)


def store_chunks(
    document_id: str,
    chunks: list[str],
    embeddings: list[list[float]]
):
    """
    Store text chunks and their corresponding embeddings.
    """

    if len(chunks) != len(embeddings):
        raise ValueError("Chunks and embeddings count must match.")

    if not chunks:
        return

    ids = [f"{document_id}_{i}" for i in range(len(chunks))]

    metadatas = [
        {
            "document_id": document_id,
            "chunk_index": i
        }
        for i in range(len(chunks))
    ]

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"Stored {len(chunks)} chunks successfully.")


def search_chunks(
    query_embedding: list[float],
    n_results: int = 3,
    document_id: str | None = None
):
    """
    Retrieve the most relevant chunks using vector similarity.
    """

    if n_results <= 0:
        raise ValueError("n_results must be greater than zero.")

    if collection.count() == 0:
        return []

    query_args = {
        "query_embeddings": [query_embedding],
        "n_results": min(n_results, collection.count())
    }

    if document_id:
        query_args["where"] = {"document_id": document_id}

    results = collection.query(**query_args)

    retrieved_chunks = []

    for i in range(len(results["ids"][0])):
        retrieved_chunks.append({
            "id": results["ids"][0][i],
            "text": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i]
        })

    return retrieved_chunks


def delete_document(document_id: str):
    """
    Delete all chunks belonging to a particular document.
    """

    collection.delete(
        where={"document_id": document_id}
    )

    print(f"Deleted document: {document_id}")
