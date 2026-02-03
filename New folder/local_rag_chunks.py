import requests
import re

def ask_qwen(context, question):
    url = "http://localhost:11434/api/generate"
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
    r = requests.post(url, json=payload)
    return r.json()["response"]

# load doc
with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.read()

# simple chunking (by sentences)
chunks = re.split(r'\n+', text)

question = "What does RAG stand for?"

# naive retrieval
best_chunk = max(
    chunks,
    key=lambda c: sum(word.lower() in c.lower() for word in question.split())
)

print(ask_qwen(best_chunk, question))
