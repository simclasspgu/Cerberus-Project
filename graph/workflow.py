from agents.retriever_agent import RetrieverAgent
from agents.reasoning_agent import ReasoningAgent
from agents.utility_agent import UtilityAgent

class GraphApp:
    def __init__(self):
        self.retriever = RetrieverAgent([])
        self.reasoner = ReasoningAgent()
        self.utility = UtilityAgent()

    def invoke(self, state):
        chunks = self.retriever.chunks
        answer = self.reasoner.answer(chunks, state.question)
        utility_output = self.utility.run_task(chunks, state.task)
        return {"answer": answer, "utility_output": utility_output}

def build_graph():
    return GraphApp()
