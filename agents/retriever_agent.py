from ingestion.chunker import DocumentChunk, chunk_text
from ingestion.loader import load_document

class RetrieverAgent:
    def __init__(self, path: str):
        self.text = load_document(path)
        self.chunks = chunk_text(self.text)

    def retrieve(self, query: str, top_k: int = 3) -> list[DocumentChunk]:
        scored_chunks = []
        for chunk in self.chunks:
            score = sum(word.lower() in chunk.text.lower() for word in query.split())
            scored_chunks.append((score, chunk))
        scored_chunks.sort(key=lambda x: x[0], reverse=True)
        top_chunks = [c for s, c in scored_chunks[:top_k] if s > 0]
        return top_chunks
