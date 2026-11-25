
from app.services.embedding_service import generate_embeddings
from app.services.vector_store_service import (
    store_chunks,
    search_chunks,
    delete_document
)

# Sample clinical chunks
chunks = [
    "The patient is a 55 year old male.",
    "His blood pressure was 150/95 mmHg.",
    "The patient was advised to monitor his blood pressure regularly."
]

document_id = "test_document_001"

# Generate embeddings
embeddings = generate_embeddings(chunks)

# Store chunks in ChromaDB
store_chunks(document_id, chunks, embeddings)

# Search using a question
query = "What was the patient's blood pressure?"
query_embedding = generate_embeddings([query])[0]

results = search_chunks(
    query_embedding,
    n_results=2,
    document_id=document_id
)

print("\nRetrieved results:")

for result in results:
    print("\nText:", result["text"])
    print("Distance:", result["distance"])
    print("Metadata:", result["metadata"])

assert len(results) > 0

print("\nVector database test PASSED!")

# Clean up test data
delete_document(document_id)
