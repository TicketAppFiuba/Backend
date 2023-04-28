from fastapi import APIRouter, Depends
from src.config.db import get_db, engine
from sqlalchemy.orm import Session
from src.schemas.event import *
from src.schemas.faq import FAQSchema, FAQDeleteSchema
from src.controllers.organizer.access import verify
from src.models.organizer import Organizer
from src.controllers.organizer.faq import *

organizer_faq = APIRouter(tags=["Organizer | FAQ"])

@organizer_faq.post("/organizer/event/faq", status_code=200)
def add(faqSchema: FAQSchema, organizer: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return add_faq_to_event(faqSchema, organizer, db)

@organizer_faq.put("/organizer/event/faq", status_code=200)
def update(faqSchema: FAQUpdateSchema, organizer: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return update_faq_to_event(faqSchema, organizer, db)

@organizer_faq.delete("/organizer/event/faq", status_code=200)
def delete(faqSchema: FAQDeleteSchema, organizer: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return delete_faq_to_event(faqSchema, organizer, db)

@organizer_faq.get("/organizer/event/faq", status_code=200)
def get(event_id: int, organizer: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return get_all_faqs_to_event(event_id, organizer, db)
