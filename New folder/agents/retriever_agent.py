import re

class RetrieverAgent:
    def __init__(self, document_path: str):
        with open(document_path, "r", encoding="utf-8") as f:
            self.text = f.read()
        self.chunks = self._chunk_text(self.text)

    def _chunk_text(self, text):
        return re.split(r'\n+', text)

    def retrieve(self, question: str, top_k: int = 1):
        scored_chunks = []

        for chunk in self.chunks:
            score = sum(
                word.lower() in chunk.lower()
                for word in question.split()
            )
            scored_chunks.append((score, chunk))

        scored_chunks.sort(reverse=True, key=lambda x: x[0])
        return [chunk for _, chunk in scored_chunks[:top_k]]
