from langchain_core.prompts import PromptTemplate
from llms.ollama_llm import get_llm
from typing import List
from agents.retriever_agent import DocumentChunk

REASONING_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a reasoning agent for a document-based QA system.

Answer the question strictly based on the provided context.
If the answer is not present in the context, say exactly:
"Not found in the document."

Context:
{context}

Question:
{question}

Answer:
"""
)
class ReasoningAgent:
    def __init__(self):
        self.llm = get_llm()

        self.chain = REASONING_PROMPT | self.llm

    def answer(self, chunks: List[DocumentChunk], question: str) -> str:
        if not chunks:
            return "I could not find relevant information in the document."

        context = "\n\n".join(chunk.text for chunk in chunks)

        result = self.chain.invoke({
            "context": context,
            "question": question
        })

        return result.strip()

