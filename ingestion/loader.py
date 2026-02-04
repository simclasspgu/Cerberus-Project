import os
from pypdf import PdfReader
from docx import Document
from PIL import Image
import pytesseract

def load_document(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    text = ""
    if ext == ".pdf":
        reader = PdfReader(path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    elif ext == ".docx":
        doc = Document(path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    elif ext in [".jpg", ".jpeg", ".png", ".tiff"]:
        img = Image.open(path)
        text = pytesseract.image_to_string(img)
    elif ext == ".txt":
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        raise ValueError("Unsupported file format")
    return text
