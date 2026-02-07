from dataclasses import dataclass

@dataclass(frozen=True)
class DocumentChunk:
    text: str
    source: str
    chunk_id: int
