from llms.ollama_llm import get_llm

class ReasoningAgent:
    def __init__(self):
        self.llm = get_llm()

    def answer(self, chunks, question: str):
        context = "\n".join([chunk.text for chunk in chunks])
        prompt = f"Document Context:\n{context}\n\nQuestion: {question}\nAnswer:"

        result = self.llm.generate([prompt])
        return result.generations[0][0].text if result.generations else "No answer generated"
