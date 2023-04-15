from sqlalchemy.orm import Session
from src.config import faq
from src.schemas.faq import *
from src.controllers.user.validations import *

def get_all_faq_from_event(event_id: int, db: Session):
    validate_event(event_id, db)
    return faq.getAllFromEvent(event_id, db)