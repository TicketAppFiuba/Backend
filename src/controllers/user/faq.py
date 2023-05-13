from sqlalchemy.orm import Session
from src.config import faq
from src.schemas.faq import *
from src.controllers.validator import validator

def get_all_faq_from_event(event_id: int, db: Session):
    validator.validate_get_event(event_id, db)
    return faq.getAllFromEvent(event_id, db)