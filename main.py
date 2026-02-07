from ingestion.loader import load_document
from ingestion.chunker import chunk_text
from agents.utility_agent import UtilityAgent
from agents.retriever_agent import RetrieverAgent
from agents.reasoning_agent import ReasoningAgent
from graph.workflow import build_graph
from graph.state import GraphState
source = "data/sample.txt"
text = load_document(source)

chunks = chunk_text(text, source=source, chunk_size=200, overlap=50)

retriever = RetrieverAgent(chunks)

question = "What is the document QA system about?"
retrieved_chunks = retriever.retrieve(question, top_k=2)
print("Retrieved:", [(c.source, c.chunk_id) for c in retrieved_chunks])

reasoner = ReasoningAgent()
answer = reasoner.answer(retrieved_chunks, question)
print("Answer:\n", answer)

utility = UtilityAgent()
summary = utility.run_task(retrieved_chunks, "summary")
translation = utility.run_task(retrieved_chunks, "translate")
checklist = utility.run_task(retrieved_chunks, "checklist")

print("\nSummary:\n", summary)
print("\nTranslation:\n", translation)
print("\nChecklist:\n", checklist)

app = build_graph(retriever)   # اگر workflow رو اصلاح کردی
state = GraphState(question=question, task="checklist")
result = app.invoke(state)
print("\nGraph Workflow Answer:\n", result["answer"])
print("Graph Utility Output:\n", result["utility_output"])
