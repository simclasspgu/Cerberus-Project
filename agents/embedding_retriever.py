from sentence_transformers import SentenceTransformer, util
from ingestion.chunker import DocumentChunk

class EmbeddingRetriever:
    def __init__(self, chunks):
        self.chunks = chunks
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = self.model.encode([chunk.text for chunk in chunks], convert_to_tensor=True)

    def retrieve(self, query, top_k=3):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_embedding, self.embeddings)[0]
        top_indices = scores.argsort(descending=True)[:top_k].tolist()
        return [self.chunks[i] for i in top_indices]
