from sqlalchemy.orm import Session
from src.controllers.validator import validator
from src.config import user

def suspend_user(email: str, db: Session):
    user_db = validator.validate_user(email, db)
    user.suspend(user_db, db)
    return {"detail": "User suspended successfully."}