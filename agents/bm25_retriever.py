from rank_bm25 import BM25Okapi
from ingestion.chunker import DocumentChunk

class BM25Retriever:
    def __init__(self, chunks):
        self.chunks = chunks
        self.corpus = [chunk.text.split() for chunk in chunks]
        self.bm25 = BM25Okapi(self.corpus)

    def retrieve(self, query, top_k=3):
        tokenized_query = query.split()
        scores = self.bm25.get_scores(tokenized_query)
        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
        return [self.chunks[i] for i in top_indices]
