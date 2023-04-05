from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.organizer import Organizer
from src.models.faq import FAQ
from src.config import event, faq
from src.schemas.faq import *

def add_question_to_event(faqSchema: FAQSchema, organizer_db: Organizer, db: Session):
    event_db = event.get(faqSchema.event_id, db)
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    if event_db.organizer_email != organizer_db.email:
        raise HTTPException(status_code=404, detail="Permission denied.")
    faq_db = faq.create(faqSchema, db)
    return {"detail": "Question created successfully", "question_id": faq_db.id}