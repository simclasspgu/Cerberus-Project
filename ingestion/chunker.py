from dataclasses import dataclass

@dataclass
class DocumentChunk:
    text: str

def chunk_text(text: str, chunk_size: int = 500) -> list[DocumentChunk]:
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk_words = words[i:i+chunk_size]
        chunks.append(DocumentChunk(" ".join(chunk_words)))
    return chunks
