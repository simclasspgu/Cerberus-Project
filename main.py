from ingestion.loader import load_document
from ingestion.chunker import chunk_text
from agents.utility_agent import UtilityAgent
from agents.retriever_agent import RetrieverAgent
from agents.reasoning_agent import ReasoningAgent
from graph.workflow import build_graph
from graph.state import GraphState

# Step 1: Load document
text = load_document("data/sample.txt")

# Step 2: Chunk document
chunks = chunk_text(text, chunk_size=1000, overlap=100)

# Step 3: Initialize Retriever
retriever = RetrieverAgent(chunks)

# Step 4: Retrieve relevant chunks
retrieved_chunks = retriever.retrieve("What is the document QA system about?", top_k=2)

# Step 5: Reasoning Agent (Ollama)
reasoner = ReasoningAgent()
answer = reasoner.answer(retrieved_chunks, "What is the document QA system about?")
print("Answer:\n", answer)

# Step 6: Utility Agent
utility = UtilityAgent()
summary = utility.run_task(retrieved_chunks, "summary")
translation = utility.run_task(retrieved_chunks, "translate")
checklist = utility.run_task(retrieved_chunks, "checklist")

print("\nSummary:\n", summary)
print("\nTranslation:\n", translation)
print("\nChecklist:\n", checklist)

# Step 7: LangGraph workflow
app = build_graph()
state = GraphState(question="What is the document QA system about?", task="checklist")
result = app.invoke(state)
print("\nGraph Workflow Answer:\n", result["answer"])
print("Graph Utility Output:\n", result["utility_output"])
