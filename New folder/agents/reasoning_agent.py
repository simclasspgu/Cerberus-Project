import requests

class ReasoningAgent:
    def __init__(self, model_url="http://localhost:11434/api/generate"):
        self.model_url = model_url

    def answer(self, chunks, question):
        context = "\n".join(chunks)
        prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}
"""
        payload = {
            "model": "qwen",
            "prompt": prompt,
            "stream": False
        }
        r = requests.post(self.model_url, json=payload)
        return r.json()["response"]
