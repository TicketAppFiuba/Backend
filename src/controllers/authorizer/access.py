from fastapi import HTTPException, Depends
from src.objects.jwt import JWTToken
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.config import authorizer
from src.models.authorizer import Authorizer
from src.schemas.user import UserSchema

jwt = JWTToken("HS256", 200)
oauth2 = OAuth2PasswordBearer(tokenUrl="/authorizer/login")

def login(schema: UserSchema, db: Session):
    user_db = authorizer.get(schema.email, db)
    if user_db is None:
        user_db = authorizer.create(schema, db)
    authorizer.update(user_db, {"login": True}, db)
    return jwt.create(schema.email)

def logout(user_db: Authorizer, db: Session):
    authorizer.update(user_db, {"login": False}, db)
    return {"response": "OK"}

def verify(token: str = Depends(oauth2), db: Session = Depends(get_db)):
    email = jwt.auth(token, authorizer, db)
    user_db = authorizer.get(email, db)
    if user_db is None or user_db.login == False:
        raise HTTPException(status_code=400, detail="Auth Error.")
    return user_db