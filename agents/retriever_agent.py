from typing import List
from agents.retriever_agent import DocumentChunk  # فرض DocumentChunk داریم

class RetrieverAgent:
    def __init__(self, document_path: str):
        text = load_document(document_path)
        self.chunks = chunk_text(text)

    def retrieve(self, question: str, top_k: int = 1) -> List[DocumentChunk]:
        # فعلاً یک نمونه ساده
        scored_chunks = []
        for chunk_text in self.chunks:
            score = sum(word.lower() in chunk_text.lower() for word in question.split())
            scored_chunks.append((score, chunk_text))

        scored_chunks.sort(reverse=True, key=lambda x: x[0])

        # حالا DocumentChunk بسازیم
        return [DocumentChunk(text=chunk, source="document", chunk_id=i)
                for i, (_, chunk) in enumerate(scored_chunks[:top_k])]
