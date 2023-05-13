from sqlalchemy.orm import Session
from src.config import complaint
from src.schemas.complaint import *
from src.controllers.validator import validator

def get_complaints(query: ComplaintQuerySchema, db: Session):
    return complaint.getAll(query, db)

def get_complaints_by_event(event_id: int, db: Session):
    validator.validate_get_event(event_id, db)
    return complaint.getAllFromEvent(event_id, db)

def get_categorys(db: Session):
    return complaint.getAllCategorys(db)