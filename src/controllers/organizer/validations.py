from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from src.config import image, event, faq
from src.models.organizer import Organizer
from src.models.event import Event
from src.models.image import Image
from src.models.faq import FAQ

def check_event(event_id: int, user_db: Organizer, db: Session):
    event_db = db.query(Event).options(joinedload(Event.sections)).filter(Event.id == event_id).first()
    check_permissions(user_db, event_db)
    return event_db

def check_img(imageSchema, user_db: Organizer, db: Session):
    #image_db = validate_img(imageSchema.id, db)
    #check_event(image_db.event_id, user_db, db)
    #return image_db
    image_db = image.get(imageSchema.id, db)
    event_db = check_event(imageSchema.event_id, user_db, db)
    check_permission_img(image_db, event_db)
    return image_db

def check_faq(faqSchema, user_db: Organizer, db: Session):
    #faq_db = validate_faq(faqSchema.id, db)
    #check_event(faq_db.event_id, user_db, db)
    #return faq_db
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
    
def validate_img(image_id: int, db: Session):
    image_db = image.get(image_id, db)
    if image_db is None:
        raise HTTPException(status_code=404, detail="Image not exist.")

def validate_faq(faq_id: int, db: Session):
    faq_db = image.get(faq_id, db)
    if faq_db is None:
        raise HTTPException(status_code=404, detail="FAQ not exist.")   