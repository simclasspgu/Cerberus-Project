from typing import List
from ingestion.chunker import DocumentChunk
from llms.ollama_llm import get_llm

class UtilityAgent:
    def __init__(self):
        self.llm = get_llm()

    def summarize(self, chunks: List[DocumentChunk]) -> str:
        text = "\n".join([c.text for c in chunks])
        prompt = f"Summarize the following text:\n{text}"
        result = self.llm.generate([prompt])
        return result.generations[0][0].text if hasattr(result, "generations") else str(result)

    def translate(self, chunks: List[DocumentChunk], target_language="fa") -> str:
        text = "\n".join([c.text for c in chunks])
        prompt = f"Translate the following text into {target_language}:\n{text}"
        result = self.llm.generate([prompt])
        return result.generations[0][0].text if hasattr(result, "generations") else str(result)

    def generate_checklist(self, chunks: List[DocumentChunk]) -> str:
        text = "\n".join([c.text for c in chunks])
        prompt = f"Generate a JSON checklist from the following text:\n{text}"
        result = self.llm.generate([prompt])
        return result.generations[0][0].text if hasattr(result, "generations") else str(result)

    def run_task(self, chunks: List[DocumentChunk], task: str):
        if task == "summary":
            return self.summarize(chunks)
        elif task == "translate":
            return self.translate(chunks)
        elif task == "checklist":
            return self.generate_checklist(chunks)
        else:
            return "Unknown task"
