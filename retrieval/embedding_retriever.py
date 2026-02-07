from sentence_transformers import SentenceTransformer, util
from ingestion.types import DocumentChunk

class EmbeddingRetriever:
    def __init__(self, chunks: list[DocumentChunk], model_name: str = "all-MiniLM-L6-v2"):
        self.chunks = chunks
        self.model = SentenceTransformer(model_name)
        self.embeddings = self.model.encode([c.text for c in chunks], convert_to_tensor=True)

    def retrieve(self, query: str, top_k: int = 3) -> list[DocumentChunk]:
        q_emb = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(q_emb, self.embeddings)[0]
        top_indices = scores.argsort(descending=True)[:top_k].tolist()
        return [self.chunks[i] for i in top_indices]
