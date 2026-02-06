class DocumentChunk:
    def __init__(self, text):
        self.text = text

def chunk_text(text, chunk_size=1000, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk_text = text[start:end]
        chunks.append(DocumentChunk(chunk_text))
        start += chunk_size - overlap
    return chunks
