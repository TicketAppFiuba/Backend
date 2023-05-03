from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.config import image, event, faq
from src.models.organizer import Organizer
from src.models.event import Event
from src.schemas.image import *
from src.schemas.faq import *

def validate_event(event_id: int, db: Session):
    event_db = event.get(event_id, db)
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    return event_db

def validate_img(image_id: int, db: Session):
    image_db = image.get(image_id, db)
    if image_db is None:
        raise HTTPException(status_code=404, detail="Image not exist.")
    return image_db

def validate_faq(faq_id: int, db: Session):
    faq_db = faq.get(faq_id, db)
    if faq_db is None:
        raise HTTPException(status_code=404, detail="FAQ not exist.")   
    return faq_db

def check_permissions(user_db: Organizer, event_db: Event):
    if user_db.email != event_db.organizer_email:
        raise HTTPException(status_code=404, detail="Permission denied.")

def check_event(event_id: int, user_db: Organizer, db: Session):
    event_db = validate_event(event_id, db)
    check_permissions(user_db, event_db)
    return event_db

def check_img(imageSchema, user_db: Organizer, db: Session):
    image_db = validate_img(imageSchema.id, db)
    check_event(image_db.event_id, user_db, db)
    return image_db

def check_faq(faqSchema, user_db: Organizer, db: Session):
    faq_db = validate_faq(faqSchema.id, db)
    check_event(faq_db.event_id, user_db, db)
    return faq_db