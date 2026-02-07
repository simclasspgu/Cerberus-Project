from agents.reasoning_agent import ReasoningAgent
from agents.utility_agent import UtilityAgent

class GraphApp:
    def __init__(self, retriever):
        self.retriever = retriever
        self.reasoner = ReasoningAgent()
        self.utility = UtilityAgent()

    def invoke(self, state):
        retrieved = self.retriever.retrieve(state.question, top_k=3)
        answer = self.reasoner.answer(retrieved, state.question)
        utility_output = self.utility.run_task(retrieved, state.task)
        return {"answer": answer, "utility_output": utility_output}

def build_graph(retriever):
    return GraphApp(retriever)
