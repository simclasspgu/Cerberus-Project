from typing import List, Optional
from pydantic import BaseModel
from models.document import DocumentChunk

class GraphState(BaseModel):
    question: str
    task: str 
    retrieved_chunks: List[DocumentChunk] = []
    answer: Optional[str] = None
    utility_output: Optional[str] = None
