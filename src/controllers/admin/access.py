from fastapi import Depends, HTTPException
from src.objects.jwt import JWTToken
from fastapi.security import OAuth2PasswordBearer

jwt = JWTToken("HS256", 200)
oauth2 = OAuth2PasswordBearer(tokenUrl="/admin/login")

def login(email: str, password: str):
    if email != "admin" or password != "admin":
        raise HTTPException(status_code=400, detail="User or password incorrect")
    return jwt.create(email)

def verify(token: str = Depends(oauth2)):
    email = jwt.basic_auth(token)
    if email != "admin":
        raise HTTPException(status_code=400, detail="Auth error")
    return email