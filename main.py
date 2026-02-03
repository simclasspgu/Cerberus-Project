from ingestion.loader import load_document
from ingestion.chunker import chunk_text
from agents.retriever_agent import RetrieverAgent
from agents.reasoning_agent import ReasoningAgent
from agents.utility_agent import UtilityAgent
text = load_document("data/sample.txt")
chunks = chunk_text(text, source="data/sample.txt")

retriever = RetrieverAgent(chunks)
retrieved_chunks = retriever.retrieve(
    "What is the document QA system about?", top_k=1
)

reasoner = ReasoningAgent()
answer = reasoner.answer(retrieved_chunks, "What is the document QA system about?")

print(answer)
utility = UtilityAgent()
summary = utility.summarize(retrieved_chunks)
print("Summary:\n", summary)