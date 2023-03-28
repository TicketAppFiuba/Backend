from fastapi import HTTPException, Depends
from objects.jwt import JWTToken
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette.config import Config
from authlib.integrations.starlette_client import OAuth
from config.db import get_db
from config.user import get, create, update
from config.user import get
from models.user import User

jwt = JWTToken("HS256", 15)
oauth2 = OAuth2PasswordBearer(tokenUrl="/login")

def login(username: str, db: Session):
    user_db = get(username, db)
    if user_db is not None and user_db.login == True:
        raise HTTPException(status_code=401, detail="You are already logged in.")
    if user_db is None:
        user_db = create(username, db)
    update(user_db, {"login": True}, db)
    return jwt.create(username)

def logout(user_db: User, db: Session):
    update(user_db, {"login": False}, db)
    return {"response": "OK"}

def verify(token: str = Depends(oauth2), db: Session = Depends(get_db)):
    username = jwt.auth(token, db)
    user_db = get(username, db)
    if user_db is None or user_db.login == False:
        raise HTTPException(status_code=400, detail="Auth Error.")
    return user_db

def generate_oauth():
    config = Config('.env')
    oauth = OAuth(config)
    NAME = 'google'
    URL = 'https://accounts.google.com/.well-known/openid-configuration'
    ARGS= {'scope': 'openid email profile'}
    oauth.register(name=NAME, server_metadata_url=URL, client_kwargs=ARGS)
    return oauth