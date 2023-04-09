from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.organizer import Organizer
from src.models.event import Event
from src.models.faq import FAQ
from src.config import event, faq
from src.schemas.faq import *
from src.controllers.organizer.event import check_permissions

def get_all_faq_from_event(event_id: int, db: Session):
    event_db = event.get(event_id, db)
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    return faq.getAllFromEvent(event_id, db)