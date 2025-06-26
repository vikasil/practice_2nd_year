from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class AuthRequest(BaseModel):
    username: str
    password: str

# GET маршрут
@app.get("/")
async def read_root():
    return {"message": "Auth service is working"}

# POST маршрут
@app.post("/auth/")
async def authenticate(auth_data: AuthRequest):
    if auth_data.username == "admin" and auth_data.password == "secret":
        return {"status": "authenticated", "username": auth_data.username}
    raise HTTPException(status_code=401, detail="Invalid credentials")