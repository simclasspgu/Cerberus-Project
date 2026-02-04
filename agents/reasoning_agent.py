from typing import List
from llms.ollama_llm import get_llm
from ingestion.chunker import DocumentChunk

class ReasoningAgent:
    def __init__(self):
        self.llm = get_llm()

    def answer(self, chunks: List[DocumentChunk], question: str) -> str:
        if not chunks:
            return "No relevant information found."
        context = "\n".join([c.text for c in chunks])
        prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        result = self.llm.generate([prompt])
        return result.generations[0][0].text if hasattr(result, "generations") else str(result)
