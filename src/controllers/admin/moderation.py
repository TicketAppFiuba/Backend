from sqlalchemy.orm import Session
from src.controllers.validator import validator

def suspend_user(email: str, db: Session):
    user_db = validator.validate_user(email, db)
    #user_db.suspended = True
    return {"detail": "User suspended successfully."}