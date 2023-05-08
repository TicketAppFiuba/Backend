from fastapi import APIRouter, HTTPException
from src.objects.jwt import JWTToken

adm_access = APIRouter(tags=["Admin | Authentication"])
jwt = JWTToken("HS256", 200)

@adm_access.post("/admin/login", status_code=200)
async def login(email: str, password: str):
    if email != "admin" or password != "admin":
        raise HTTPException(status_code=400, detail="User or password incorrect")
    return jwt.create(email)
