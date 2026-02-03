from agents.retriever_agent import RetrieverAgent
from agents.reasoning_agent import ReasoningAgent

# ساخت Retriever
retriever = RetrieverAgent("notes.txt")
chunks = retriever.retrieve("What does RAG stand for?", top_k=2)

# ساخت Reasoning Agent
reasoner = ReasoningAgent()
answer = reasoner.answer(chunks, "What does RAG stand for?")

print(answer)
