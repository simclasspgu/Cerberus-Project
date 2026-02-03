
from typing import List
from agents.retriever_agent import DocumentChunk


class ReasoningAgent:
    def answer(self, chunks: List[DocumentChunk], question: str) -> str:
        if not chunks:
            return "I could not find relevant information in the document."

        context = "\n".join(chunk.text for chunk in chunks)

        answer = (
            "Based on the retrieved document sections, here is the relevant information:\n\n"
            f"{context}"
        )

        return answer