from ingestion.document import DocumentChunk

def chunk_text(
    text: str,
    source: str,
    chunk_size: int = 500,
    overlap: int = 100
):
    chunks = []
    start = 0
    chunk_id = 0

    while start < len(text):
        end = start + chunk_size
        chunk_text = text[start:end]

        chunks.append(
            DocumentChunk(
                text=chunk_text,
                source=source,
                chunk_id=chunk_id
            )
        )

        start = end - overlap
        chunk_id += 1

    return chunks
