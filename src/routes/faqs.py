from fastapi import APIRouter, Depends
from src.config.db import get_db, engine
from sqlalchemy.orm import Session
from src.models import faq
from src.models.organizer import Organizer
from src.schemas.event import *
from src.schemas.faq import *
from src.controllers.organizer_access import verify
from src.controllers.faq import add_faq_to_event, update_faq_to_event, delete_faq_to_event

router = APIRouter(tags=["Event Faqs | Organizer"])
faq.Base.metadata.create_all(bind=engine)

@router.post("/event/faqs/add", status_code=200)
def add(faq: FaqSchema, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return add_faq_to_event(faq, user_db, db)

@router.put("/event/faqs/update", status_code=200)
def update(faq: FaqUpdateSchema, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return update_faq_to_event(faq, user_db, db)

@router.delete("/event/faqs/delete", status_code=200)
def delete(faq: FaqDeleteSchema, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return delete_faq_to_event(faq, user_db, db)