from langchain_ollama import OllamaLLM

def get_llm():
    return OllamaLLM(
        model="qwen:latest",
        temperature=0,
        verbose=True
    )
