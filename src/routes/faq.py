from fastapi import APIRouter, Depends
from src.config.db import get_db, engine
from sqlalchemy.orm import Session
from src.schemas.event import *
from src.schemas.faq import FAQSchema, FAQDeleteSchema
from src.controllers.organizer.access import verify
from src.models.organizer import Organizer
from src.controllers.organizer.faq import *

router = APIRouter(tags=["Event FAQ | Organizer"])

@router.post("/organizer/event/faq", status_code=200)
def add(faqSchema: FAQSchema, organizer: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return add_faq_to_event(faqSchema, organizer, db)

@router.put("/organizer/event/faq", status_code=200)
def update(faqSchema: FAQUpdateSchema, organizer: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return update_faq_to_event(faqSchema, organizer, db)

@router.delete("/organizer/event/faq", status_code=200)
def delete(faqSchema: FAQDeleteSchema, organizer: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return delete_faq_to_event(faqSchema, organizer, db)

@router.get("/organizer/event/faq", status_code=200)
def get(event_id: int, organizer: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return get_all_faqs_to_event(event_id, organizer, db)
