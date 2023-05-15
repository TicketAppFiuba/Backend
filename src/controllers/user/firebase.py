from sqlalchemy.orm import Session
from src.schemas.complaint import *
from src.controllers.user import permissions
from src.config import complaint
from src.models.user import User

def set_firebase_token(token: str, user_db: User, db: Session):
    user_db.firebase_token = token
    db.commit()