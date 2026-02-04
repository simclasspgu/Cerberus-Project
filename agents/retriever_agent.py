from typing import List
from models.document import DocumentChunk
from ingestion.loader import load_document
from ingestion.chunker import chunk_text

class RetrieverAgent:
    def __init__(self, document_path: str):
        text = load_document(document_path)
        self.chunks = chunk_text(text, source=document_path)

    def retrieve(self, query: str, top_k: int = 2) -> List[DocumentChunk]:
        scored = []

        for i, chunk in enumerate(self.chunks):
            score = sum(
                word.lower() in chunk.text.lower()
                for word in query.split()
            )
            scored.append((score, chunk, i))

        scored.sort(reverse=True, key=lambda x: x[0])

        return [
            DocumentChunk(
                text=chunk.text,
                source=chunk.source,
                chunk_id=chunk.chunk_id
            )
            for _, chunk, _ in scored[:top_k]
        ]
