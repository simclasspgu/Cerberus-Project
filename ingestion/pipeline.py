from ingestion.loader import load_document
from ingestion.chunker import chunk_text

def ingest_document(path: str):
    text = load_document(path)
    chunks = chunk_text(text, source=path)
    return chunks
