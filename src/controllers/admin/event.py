from sqlalchemy.orm import Session
from src.config import image, faq, section
from src.schemas.image import *
from src.controllers.validator import validator

def get_event(event_id: int, db: Session):
    event_db = validator.validate_event(event_id, db)
    images_db = image.getAllFromEvent(event_id, db)
    faq_db = faq.getAllFromEvent(event_id, db)
    diary_db = section.getAllFromEvent(event_id, db)
    return {"Event": event_db, "Images": images_db, "FAQ": faq_db, "Diary": diary_db}