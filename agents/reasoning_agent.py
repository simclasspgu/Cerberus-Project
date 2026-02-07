from llms.ollama_llm import get_llm

class ReasoningAgent:
    def __init__(self):
        self.llm = get_llm()

    def answer(self, chunks, question: str):
        if not chunks:
            return "I couldn't find relevant information in the document."

        context = "\n\n".join(
            [f"[{c.source}#{c.chunk_id}]\n{c.text}" for c in chunks]
        )

        prompt = f"""You are a document QA assistant.
Answer the question ONLY using the provided context.
If the answer is not in the context, say: "Not found in the document."
Cite sources using the bracket ids like [source#chunk_id].

Context:
{context}

Question: {question}
Answer:"""

        result = self.llm.generate([prompt])
        text = result.generations[0][0].text if result.generations else "No answer generated"

        sources = ", ".join([f"{c.source}#{c.chunk_id}" for c in chunks])
        return f"{text.strip()}\n\nSources: {sources}"
