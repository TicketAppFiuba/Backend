from sqlalchemy.orm import Session
from src.controllers.validator import validator
from src.config import user
from src.config import event
from src.config import suspension

def suspend_user(email: str, db: Session):
    user_db = validator.validate_user(email, db)
    user.suspend(user_db, db)
    suspension.create(db)
    return {"detail": "User suspended successfully."}

def suspend_event(event_id: int, db: Session):
    user_db = validator.validate_event(event_id, db)
    event.suspend(user_db, db)
    return {"detail": "Event suspended successfully."}

def enable_user(email: str, db: Session):
    user_db = validator.validate_user(email, db)
    user.enable(user_db, db)
    return {"detail": "User enabled successfully."}

def enable_event(event_id: int, db: Session):
    user_db = validator.validate_event(event_id, db)
    event.enable(user_db, db)
    return {"detail": "Event enabled successfully."}