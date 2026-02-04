class GraphState:
    def __init__(self, question, task):
        self.question = question
        self.task = task  # "summary" | "translate" | "checklist"
