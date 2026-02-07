FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# 0) سرعت و پایداری نصب: mirror + timeout
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip config set global.default-timeout 180

# 1) پیش‌نیازهای torch را از mirror نصب کن (تا نره pythonhosted)
RUN pip install --no-cache-dir \
    filelock typing-extensions sympy networkx jinja2 fsspec

# 2) torch CPU-only را از index رسمی pytorch نصب کن
RUN pip install --no-cache-dir \
    --index-url https://download.pytorch.org/whl/cpu \
    torch

# 3) بقیه requirements از mirror
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
