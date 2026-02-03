from typing import List
from dataclasses import dataclass


@dataclass
class DocumentChunk:
    text: str
    source: str
    chunk_id: int


class RetrieverAgent:
    def __init__(self, chunks: List[DocumentChunk]):
        self.chunks = chunks

    def retrieve(self, query: str, top_k: int = 2) -> List[DocumentChunk]:
        query_words = set(query.lower().split())

        scored = []
        for chunk in self.chunks:
            chunk_words = set(chunk.text.lower().split())
            score = len(query_words & chunk_words)
            scored.append((score, chunk))

        scored.sort(key=lambda x: x[0], reverse=True)

        return [chunk for score, chunk in scored[:top_k]]