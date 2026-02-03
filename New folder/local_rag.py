import requests

def ask_qwen(context, question):
    url = "http://localhost:11434/api/generate"
    prompt = f"""
Use ONLY the following context to answer the question.

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

    r = requests.post(url, json=payload)
    return r.json()["response"]

# load document
with open("notes.txt", "r", encoding="utf-8") as f:
    context = f.read()

answer = ask_qwen(context, "What does RAG stand for?")
print(answer)
