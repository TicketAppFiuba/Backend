from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.organizer import Organizer
from src.models.event import Event
from src.models.faq import Faq
from src.config import event, faq
from src.schemas.faq import *
from src.controllers.event import check_permissions

def add_faq_to_event(faqSchema: FaqSchema, user_db: Organizer, db: Session):
    event_db = event.get(faqSchema.event_id, db)
    check_permissions(user_db, event_db)
    faq_db = faq.create(faqSchema, db)
    return faq_db

def update_faq_to_event(faqSchema: FaqUpdateSchema, user_db: Organizer, db: Session):
    event_db = event.get(faqSchema.event_id, db)
    check_permissions(user_db, event_db)
    faq_db = faq.get(faqSchema.id, db)
    check_permission_faq(faq_db, event_db)
    return faq.update(faq_db, faqSchema, db)

def delete_faq_to_event(faqSchema: FaqSchema, user_db: Organizer, db: Session):
    event_db = event.get(faqSchema.event_id, db)
    check_permissions(user_db, event_db)
    faq_db = faq.get(faqSchema.id, db)
    check_permission_faq(faq_db, event_db)
    return faq.delete(faq_db, db)

def check_permission_faq(faq_db: Faq, event_db: Event):
    if faq_db is None:
        raise HTTPException(status_code=404, detail="Faq not exist.")
    if faq_db.event_id != event_db.id:
        raise HTTPException(status_code=404, detail="Not permission.")