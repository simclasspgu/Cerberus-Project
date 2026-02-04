from agents.retriever_agent import RetrieverAgent
from agents.reasoning_agent import ReasoningAgent
from agents.utility_agent import UtilityAgent

class GraphApp:
    def __init__(self):
        self.retriever = None
        self.reasoner = ReasoningAgent()
        self.utility = UtilityAgent()

    def invoke(self, state):
        question = state.get("question")
        task = state.get("task")

        chunks = self.retriever.chunks if self.retriever else []

        answer = self.reasoner.answer(chunks, question)
        utility_output = self.utility.run_task(chunks, task)

        return {"answer": answer, "utility_output": utility_output}

def build_graph(file_path=None):
    app = GraphApp()
    if file_path:
        app.retriever = RetrieverAgent(file_path)
    return app
