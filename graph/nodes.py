from graph.state import GraphState
from agents.retriever_agent import RetrieverAgent
from agents.reasoning_agent import ReasoningAgent
from agents.utility_agent import UtilityAgent

retriever = RetrieverAgent("data/sample.txt")
reasoner = ReasoningAgent()
utility = UtilityAgent()

def retriever_node(state: GraphState) -> GraphState:
    chunks = retriever.retrieve(state.question, top_k=3)
    state.retrieved_chunks = chunks
    return state

def reasoning_node(state: GraphState) -> GraphState:
    answer = reasoner.answer(state.retrieved_chunks, state.question)
    state.answer = answer
    return state

def utility_node(state: GraphState) -> GraphState:
    output = utility.run_task(state.retrieved_chunks, state.task)
    state.utility_output = output
    return state

def fallback_node(state: GraphState) -> GraphState:
    state.answer = "No relevant information found in the document."
    return state
