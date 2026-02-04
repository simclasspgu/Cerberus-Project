from ingestion.loader import load_document
from ingestion.chunker import chunk_text
from agents.utility_agent import UtilityAgent
from agents.retriever_agent import RetrieverAgent
from agents.reasoning_agent import ReasoningAgent

retriever = RetrieverAgent("data/sample.txt")
retrieved_chunks = retriever.retrieve("What is the document QA system about?", top_k=2)

reasoner = ReasoningAgent()
answer = reasoner.answer(retrieved_chunks, "What is the document QA system about?")
print("Answer:")
print(answer)

utility = UtilityAgent()
print("\nSummary:")
print(utility.run_task(retrieved_chunks, "summary"))

print("\nTranslation:")
print(utility.run_task(retrieved_chunks, "translate"))

print("\nChecklist:")
print(utility.run_task(retrieved_chunks, "checklist"))
