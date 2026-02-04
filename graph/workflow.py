from langgraph.graph import StateGraph, END
from graph.state import GraphState
from graph.nodes import (
    retriever_node,
    reasoning_node,
    utility_node,
    fallback_node
)

def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("retrieve", retriever_node)
    graph.add_node("reason", reasoning_node)
    graph.add_node("utility", utility_node)
    graph.add_node("fallback", fallback_node)

    graph.set_entry_point("retrieve")

    graph.add_conditional_edges(
        "retrieve",
        lambda state: "fallback" if not state.retrieved_chunks else "reason"
    )

    graph.add_conditional_edges(
        "reason",
        lambda state: "utility" if state.task != "qa" else END
    )

    graph.add_edge("utility", END)
    graph.add_edge("fallback", END)

    return graph.compile()
