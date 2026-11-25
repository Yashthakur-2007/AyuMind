
from app.services.embedding_service import generate_embeddings

chunks = [
    "The patient is a 55 year old male.",
    "His blood pressure was 150/95 mmHg.",
    "The patient was advised to monitor his blood pressure regularly."
]

embeddings = generate_embeddings(chunks)

print("Number of chunks:", len(chunks))
print("Number of embeddings:", len(embeddings))

for i, embedding in enumerate(embeddings):
    print(f"Embedding {i + 1} dimensions:", len(embedding))

assert len(embeddings) == len(chunks)
assert all(len(embedding) == 384 for embedding in embeddings)

print("\nEmbedding test PASSED!")
