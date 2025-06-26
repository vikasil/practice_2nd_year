from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Модель для пользователя
class User(BaseModel):
    id: int
    name: str
    email: str

users_db = {
    1: {"id": 1, "name": "Tori Sil", "email": "tori@example.com"},
    2: {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
}

# GET маршрут для получения всех пользователей
@app.get("/")
async def read_root():
    return {"message": "Users service is working"}

# GET маршрут для получения конкретного пользователя
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

# POST маршрут для создания пользователя
@app.post("/users/")
async def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.id] = user.dict()
    return {"status": "created", "user": user.dict()}