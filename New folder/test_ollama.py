import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen",
    "prompt": "Explain Retrieval Augmented Generation in one sentence",
    "stream": False
}

response = requests.post(url, json=payload)
print(response.json()["response"])
