from llms.ollama_llm import get_llm

class UtilityAgent:
    def __init__(self):
        self.llm = get_llm()

    def run_task(self, chunks, task_type):
        context = "\n".join([chunk.text for chunk in chunks])

        if task_type == "summary":
            prompt = f"Summarize the following text:\n{context}"
            result = self.llm.generate([prompt])
            return result.generations[0][0].text if result.generations else ""
        
        elif task_type == "translate":
            prompt = f"Translate the following text to Persian:\n{context}"
            result = self.llm.generate([prompt])
            return result.generations[0][0].text if result.generations else ""
        
        elif task_type == "checklist":
            # برای simplicity یک نمونه خروجی ثابت می‌ده
            return [{"task": "Split original text into smaller sections", "done": False}]
        
        else:
            return ""
