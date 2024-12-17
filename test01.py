from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import JSONResponse
import os
import json

app = FastAPI()

# 檔案儲存目錄
BASE_DIR = "./user_files"
os.makedirs(BASE_DIR, exist_ok=True)

# POST API: 儲存用戶資料到檔案
@app.post("/user/add")
async def add_user(id: str = Form(...), name: str = Form(...)):
    file_path = os.path.join(BASE_DIR, f"user_{id}.json")
    user_data = {"id": id, "name": name }
    with open(file_path, "w") as f:
        json.dump(user_data, f)
    return {"message": f"User {id} saved successfully.", "data": user_data}

# GET API: 列出所有 user_{id}.json 文件
@app.get("/users")
def list_users():
    files = [f for f in os.listdir(BASE_DIR) if f.startswith("user_") and f.endswith(".json")]
    return {"files": files}

# GET API: 查詢特定 user_{id}.json 文件內容
@app.get("/user/{user_id}")
def get_user(user_id: str):
    file_path = os.path.join(BASE_DIR, f"user_{user_id}.json")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"User file user_{user_id}.json not found.")
    with open(file_path, "r") as f:
        user_data = json.load(f)
    return {"user_data": user_data}

@app.get("/")
def read_root():
    return {"message": "Hello World"}