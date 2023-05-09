from fastapi import APIRouter
from src.controllers.admin import access

adm_access = APIRouter(tags=["Admin | Authentication"])

@adm_access.post("/admin/login", status_code=200)
async def login(email: str, password: str):
    return access.login(email, password)
