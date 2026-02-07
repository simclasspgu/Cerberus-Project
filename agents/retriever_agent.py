from ingestion.types import DocumentChunk
from retrieval.bm25_retriever import BM25Retriever
from retrieval.embedding_retriever import EmbeddingRetriever

class RetrieverAgent:
    def __init__(self, chunks: list[DocumentChunk]):
        self.chunks = chunks
        self.bm25 = BM25Retriever(chunks)
        self.embed = EmbeddingRetriever(chunks)

    def retrieve(self, query: str, top_k: int = 3) -> list[DocumentChunk]:
        # از هر دو روش نتیجه بگیر
        bm25_hits = self.bm25.retrieve(query, top_k=top_k)
        emb_hits = self.embed.retrieve(query, top_k=top_k)

        # merge بدون تکراری (با کلید source+chunk_id)
        merged = []
        seen = set()

        for ch in (bm25_hits + emb_hits):
            key = (ch.source, ch.chunk_id)
            if key not in seen:
                seen.add(key)
                merged.append(ch)

        # خروجی نهایی
        return merged[:top_k]
