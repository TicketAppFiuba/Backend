from fastapi import APIRouter, Depends, HTTPException
from src.config.db import get_db, engine
from sqlalchemy.orm import Session
from src.models.user import User
from starlette.requests import Request
from src.controllers.user import access
from src.schemas.user import UserSchema
import requests

user_access = APIRouter(tags=["User | Authentication"])

@user_access.get("/user/login", status_code=200)
async def login(name: str, email: str, db: Session = Depends(get_db)):
    #url = 'https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={}'.format(token)
    #response = requests.get(url)
    #if response.status_code != 200:
    #     raise HTTPException(status_code=400, detail="JWT Invalid.")    
    user = UserSchema(name=name, email=email)
    return access.login(user, db)

@user_access.get("/user/logout", status_code=200)
async def logout(request: Request, user_db: User = Depends(access.verify), db: Session = Depends(get_db)):
    for key in list(request.session.keys()):
        request.session.pop(key)
    return access.logout(user_db, db)

