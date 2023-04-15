from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.config import image, event, faq
from src.models.organizer import Organizer
from src.models.event import Event
from src.models.image import Image
from src.models.faq import FAQ

def check_event(event_id: int, user_db: Organizer, db: Session):
    event_db = event.get(event_id, db)
    check_permissions(user_db, event_db)
    return event_db

def check_img(imageSchema, user_db: Organizer, db: Session):
    image_db = image.get(imageSchema.id, db)
    event_db = check_event(imageSchema.event_id, user_db, db)
    check_permission_img(image_db, event_db)
    return image_db

def check_faq(faqSchema, user_db: Organizer, db: Session):
    faq_db = faq.get(faqSchema.id, db)
    event_db = check_event(faqSchema.event_id, user_db, db)
    check_permission_faq(faq_db, event_db)
    return faq_db

def check_permissions(user_db: Organizer, event_db: Event):
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    if user_db.email != event_db.organizer_email:
        raise HTTPException(status_code=404, detail="Permission denied.")

def check_permission_img(image_db: Image, event_db: Event):
    if image_db is None:
        raise HTTPException(status_code=404, detail="Image not exist.")
    if image_db.event_id != event_db.id:
        raise HTTPException(status_code=404, detail="Not permission.")
        
def check_permission_faq(faq_db: FAQ, event_db: Event):
    if faq_db is None:
        raise HTTPException(status_code=404, detail="FAQ not exist.")
    if faq_db.event_id != event_db.id:
        raise HTTPException(status_code=404, detail="Not permission.")