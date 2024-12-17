# 選擇基礎 Python 映像檔
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 複製 test01.py 到容器內
COPY test01.py .

# 設定執行的指令 (根據 test01.py 的執行邏輯修改)
CMD ["python", "test01.py"]

