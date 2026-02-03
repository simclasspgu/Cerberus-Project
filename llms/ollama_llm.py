from langchain_community.llms import Ollama

def get_llm():
    return Ollama(
        model="qwen:latest",
        temperature=0.2
    )
