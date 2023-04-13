from fastapi import HTTPException, Depends
from src.objects.jwt import JWTToken
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.config import user
from src.models.user import User
from src.schemas.user import UserSchema

jwt = JWTToken("HS256", 15)
oauth2 = OAuth2PasswordBearer(tokenUrl="/user/login")

def login(schema: UserSchema, db: Session):
    user_db = user.get(schema.email, db)
    if user_db is None:
        user_db = user.create(schema, db)
    user.update(user_db, {"login": True}, db)
    return jwt.create(schema.email)

def logout(user_db: User, db: Session):
    user.update(user_db, {"login": False}, db)
    return {"response": "OK"}

def verify(token: str = Depends(oauth2), db: Session = Depends(get_db)):
    email = jwt.auth(token, user, db)
    user_db = user.get(email, db)
    if user_db is None or user_db.login == False:
        raise HTTPException(status_code=400, detail="Auth Error.")
    return user_db
