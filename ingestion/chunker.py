from ingestion.types import DocumentChunk  # یا اگر همینجا تعریفش کردی، همون import لازم نیست

def chunk_text(text: str, source: str, chunk_size=1000, overlap=100):
    chunks = []
    start = 0
    chunk_id = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        piece = text[start:end]

        chunks.append(DocumentChunk(
            text=piece,
            source=source,
            chunk_id=chunk_id
        ))

        chunk_id += 1
        start += chunk_size - overlap

    return chunks
