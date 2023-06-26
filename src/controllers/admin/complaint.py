from sqlalchemy.orm import Session
from src.config import complaint
from src.schemas.complaint import *
from src.controllers.validator import validator

def get_complaints(query: ComplaintQuerySchema, db: Session):
    return complaint.getAll(query, db)
    
def get_complaints_users(query: ComplaintQuerySchema, db: Session):
    return complaint.getAllUsers(query, db)    

def get_complaints_by_event(event_id: int, db: Session):
    validator.validate_event(event_id, db)
    return complaint.getAllFromEvent(event_id, db)

def get_complaints_by_user(email: str, db: Session):
    user_db = validator.validate_user(email, db)
    return complaint.getAllFromUser(user_db.id, db)

def get_categorys(db: Session):
    return complaint.getAllCategorys(db)
