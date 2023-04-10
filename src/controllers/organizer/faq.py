from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.organizer import Organizer
from src.models.event import Event
from src.models.faq import FAQ
from src.config import event, faq
from src.schemas.faq import *
from src.controllers.organizer.event import check_permissions

def add_faq_to_event(faqSchema: FAQSchema, user_db: Organizer, db: Session):
    event_db = event.get(faqSchema.event_id, db)
    check_permissions(user_db, event_db)
    faq_db = faq.create(faqSchema, db)
    return {"detail": "FAQ created successfully", "id": faq_db.id}

def update_faq_to_event(faqSchema: FAQUpdateSchema, user_db: Organizer, db: Session):
    event_db = event.get(faqSchema.event_id, db)
    check_permissions(user_db, event_db)
    faq_db = faq.get(faqSchema.id, db)
    check_permission_faq(faq_db, event_db)
    faq_dict = faqSchema.dict(exclude_unset=True, exclude_none=True, exclude={'id'})
    faq.update(faq_db, faq_dict, db)
    return {"detail": "FAQ modified successfully."}

def delete_faq_to_event(faqSchema: FAQDeleteSchema, user_db: Organizer, db: Session):
    event_db = event.get(faqSchema.event_id, db)
    check_permissions(user_db, event_db)
    faq_db = faq.get(faqSchema.id, db)
    check_permission_faq(faq_db, event_db)
    faq.delete(faq_db, db)
    return {"detail": "FAQ deleted successfully."}

def check_permission_faq(faq_db: FAQ, event_db: Event):
    if faq_db is None:
        raise HTTPException(status_code=404, detail="Faq not exist.")
    if faq_db.event_id != event_db.id:
        raise HTTPException(status_code=404, detail="Not permission.")
