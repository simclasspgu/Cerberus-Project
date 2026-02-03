from typing import List
from llms.ollama_llm import get_llm
from agents.retriever_agent import DocumentChunk

class UtilityAgent:
    def __init__(self):
        # LLM رو از تابعی که قبلاً ساختیم می‌گیریم
        self.llm = get_llm()

    def run_task(self, chunks: List[DocumentChunk], task: str) -> str:
        """
        chunks: متن‌های تقسیم شده‌ی سند
        task: نوع کاربر
              'summary' -> خلاصه
              'translate' -> ترجمه فارسی
              'checklist' -> ساخت checklist
        """
        # اگر سند خالی بود
        if not chunks:
            return "No document content found."

        # متن کامل سند
        context = "\n".join(chunk.text for chunk in chunks)

        # بسته به task، prompt می‌سازیم
        if task.lower() == "summary":
            prompt = f"Summarize the following text concisely:\n\n{context}"
        elif task.lower() == "translate":
            prompt = f"Translate the following text to Persian:\n\n{context}"
        elif task.lower() == "checklist":
            prompt = (
                f"From the following text, create a checklist of tasks in JSON format. "
                f"Each task should have 'task' and 'done' keys.\n\n{context}"
            )
        else:
            return f"Unknown task: {task}"

        # LLM رو صدا می‌زنیم
        response = self.llm.generate(prompt)
        return response
