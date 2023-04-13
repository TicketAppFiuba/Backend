from fastapi import HTTPException, Depends
from src.objects.jwt import JWTToken
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.config import organizer
from src.models.organizer import Organizer
from src.schemas.user import UserSchema

jwt = JWTToken("HS256", 200)
oauth2 = OAuth2PasswordBearer(tokenUrl="/organizer/login")

def login(schema: UserSchema, db: Session):
    user_db = organizer.get(schema.email, db)
    if user_db is None:
        user_db = organizer.create(schema, db)
    organizer.update(user_db, {"login": True}, db)
    return jwt.create(schema.email)

def logout(user_db: Organizer, db: Session):
    organizer.update(user_db, {"login": False}, db)
    return {"response": "OK"}

def verify(token: str = Depends(oauth2), db: Session = Depends(get_db)):
    email = jwt.auth(token, organizer, db)
    user_db = organizer.get(email, db)
    if user_db is None or user_db.login == False:
        raise HTTPException(status_code=400, detail="Auth Error.")
    return user_db