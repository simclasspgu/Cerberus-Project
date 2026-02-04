from typing import List
from models.document import DocumentChunk
from llms.ollama_llm import get_llm

class UtilityAgent:
    def __init__(self):
        self.llm = get_llm()

    def run_task(self, chunks: List[DocumentChunk], task: str) -> str:
        if not chunks:
            return "No document content found."

        context = "\n".join(chunk.text for chunk in chunks)

        if task.lower() == "summary":
            prompt = f"""
Summarize the following text concisely:

{context}
"""
        elif task.lower() == "translate":
            prompt = f"""
You are a professional technical translator.

Translate the following English text into clear, accurate Persian.
Preserve the original meaning.
Do NOT summarize.
Do NOT add or remove information.
Only output the translation.


{context}
"""
        elif task.lower() == "checklist":
            prompt = f"""
You are an information extraction system.

Extract ALL actionable tasks from the text below.

Rules:
- Output MUST be a JSON array
- Each task must be explicit and distinct
- Each item must contain:
  - "task": string
  - "done": false
- Do NOT explain
- Do NOT summarize
- Do NOT output anything outside JSON

Text:
{context}
"""
        else:
            return f"Unknown task: {task}"

        return self.llm.invoke(prompt)
