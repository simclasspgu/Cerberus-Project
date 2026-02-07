from ingestion.loader import load_document
from ingestion.chunker import chunk_text
from ingestion.types import DocumentChunk

def ingest_document(path: str) -> list[DocumentChunk]:
    text = load_document(path)
    chunks = chunk_text(text, source=path)
    return chunks
