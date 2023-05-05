from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.organizer import Organizer
from src.controllers.validator import validator

def check_event(event_id: int, user_db: Organizer, db: Session):
    event_db = validator.validate_event(event_id, db)
    if user_db.email != event_db.organizer_email:
        raise HTTPException(status_code=404, detail="Permission denied.")
    return event_db

def check_img(imageSchema, user_db: Organizer, db: Session):
    image_db = validator.validate_image(imageSchema.id, db)
    check_event(image_db.event_id, user_db, db)
    return image_db

def check_faq(faqSchema, user_db: Organizer, db: Session):
    faq_db = validator.validate_faq(faqSchema.id, db)
    check_event(faq_db.event_id, user_db, db)
    return faq_db