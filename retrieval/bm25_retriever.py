from rank_bm25 import BM25Okapi
from ingestion.types import DocumentChunk

class BM25Retriever:
    def __init__(self, chunks: list[DocumentChunk]):
        self.chunks = chunks
        self.corpus = [chunk.text.split() for chunk in chunks]
        self.bm25 = BM25Okapi(self.corpus)

    def retrieve(self, query: str, top_k: int = 3) -> list[DocumentChunk]:
        tokenized_query = query.split()
        scores = self.bm25.get_scores(tokenized_query)
        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
        return [self.chunks[i] for i in top_indices]
