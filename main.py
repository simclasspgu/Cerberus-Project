from ingestion.loader import load_document
from ingestion.chunker import chunk_text
from agents.utility_agent import UtilityAgent
from agents.retriever_agent import RetrieverAgent
from agents.reasoning_agent import ReasoningAgent
from graph.workflow import build_graph
from graph.state import GraphState

# Retriever
retriever = RetrieverAgent("data/sample.txt")
retrieved_chunks = retriever.retrieve("What is the document QA system about?", top_k=2)

# Reasoning
reasoner = ReasoningAgent()
answer = reasoner.answer(retrieved_chunks, "What is the document QA system about?")
print("Answer:")
print(answer)

# Utility Agent
utility = UtilityAgent()

print("\nSummary:")
print(utility.run_task(retrieved_chunks, "summary"))

print("\nTranslation:")
print(utility.run_task(retrieved_chunks, "translate"))

print("\nChecklist:")
print(utility.run_task(retrieved_chunks, "checklist"))
app = build_graph()

state = GraphState(
    question="What is the document QA system about?",
    task="checklist"  # qa | summary | translate | checklist
)

result = app.invoke(state)

print("Answer:", result["answer"])
print("Utility Output:", result["utility_output"])