import os
from langchain_ollama import OllamaLLM

def get_llm():
    base_url = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")

    return OllamaLLM(
        model="qwen:latest",
        base_url=base_url,
        temperature=0,
        verbose=True
    )
