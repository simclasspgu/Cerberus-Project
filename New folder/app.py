# app.py

# 1️⃣ مسیر فایل متنی
file_path = "data/example.txt"

# 2️⃣ خواندن فایل
try:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print(f"File {file_path} not found! Make sure the file exists in the 'data' folder.")
    exit()

# 3️⃣ چاپ متن اصلی
print("=== Original Text ===")
print(text)

# 4️⃣ تقسیم متن به تکه‌ها (Chunking)
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,     # تعداد کاراکتر در هر تکه
    chunk_overlap=10   # تعداد کاراکتر همپوشانی بین تکه‌ها
)

chunks = splitter.split_text(text)

# 5️⃣ چاپ تکه‌ها
print("\n=== Text Chunks ===")
for i, chunk in enumerate(chunks, 1):
    print(f"{i}: {chunk}")
