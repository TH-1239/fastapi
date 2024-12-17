# 使用 Python 3.11 作為基礎映像
FROM python:3.11-slim

# 設置工作目錄
WORKDIR /app

# 複製程式碼到容器
COPY . .

# 安裝 FastAPI 和 Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn python-multipart

# 指定容器啟動命令
CMD ["uvicorn", "test01:app", "--host", "0.0.0.0", "--port", "8000"]