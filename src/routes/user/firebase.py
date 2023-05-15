from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.controllers.user.access import verify
from src.models.user import User
from src.controllers.user.firebase import set_firebase_token

firebase = APIRouter(tags=["Firebase | Users"])

@firebase.get("/user/firebase_token", status_code=200)
def firebase_token(user_db: User = Depends(verify)):
    return { "firebase_token": user_db.firebase_token }

@firebase.put("/user/firebase_token", status_code=204)
def firebase_token(token: str, user_db: User = Depends(verify), db: Session = Depends(get_db)):
    set_firebase_token(token, user_db, db)
    return { "firebase_token": user_db.firebase_token }
