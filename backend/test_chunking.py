from app.services.chunking_service import chunk_text


text = """
The patient is a 55 year old male.

His blood pressure was 150/95 mmHg.

The patient was advised to monitor his blood pressure regularly.

He returned after two weeks for follow-up.
"""

chunks = chunk_text(
    text,
    chunk_size=60,
    overlap=10
)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)