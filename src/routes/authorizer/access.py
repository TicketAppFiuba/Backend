from fastapi import APIRouter, Depends, HTTPException
from src.config.db import get_db
from sqlalchemy.orm import Session
from src.controllers.authorizer import access
from src.models.organizer import Organizer
from starlette.requests import Request
from src.schemas.user import UserSchema
from google.auth.transport import requests
import requests

authorizer_access = APIRouter(tags=["Authorizer | Authentication"])

@authorizer_access.get("/authorizer/login", status_code=200)
async def login(token: str, db: Session = Depends(get_db)):
    url = 'https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={}'.format(token)
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="JWT Invalid.")    
    user = UserSchema(name=response.json()["name"], email=response.json()["email"])
    return access.login(user, db)

@authorizer_access.get("/authorizer/logout", status_code=200)
async def logout(request: Request, user_db: Organizer = Depends(access.verify), db: Session = Depends(get_db)):
    for key in list(request.session.keys()):
        request.session.pop(key)
    return access.logout(user_db, db)