from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.organizer import Organizer
from src.models.event import Event
from src.schemas.event import EventSchema, EventSchemaUpdate
from src.config import event
from src.schemas.image import *
from src.config import image

def create_event(eventSchema: EventSchema, user_db: Organizer, db: Session):
    return event.create(eventSchema, user_db.email, db)

def update_event(eventSchema: EventSchemaUpdate, user_db: Organizer, db: Session):
    event_db = event.get(eventSchema.id, db)
    check_permissions(user_db, event_db)
    event_dict = eventSchema.dict(exclude_unset=True, exclude_none=True, exclude={'id'})
    return event.update(event_db, event_dict, db)

def delete_event(event_id: int, user_db: Organizer, db: Session):
    event_db = event.get(event_id, db)
    check_permissions(user_db, event_db)
    event.delete(event_db, db)
    return {"detail": "OK"}

def get_event(event_id: int, user_db: Organizer, db: Session):
    event_db = event.get(event_id, db)
    check_permissions(user_db, event_db)
    image_db = image.getAllFromEvent(event_id, db)
    return event_db, image_db

def get_events_from(user_db: Organizer, db: Session):
    return event.getAllEventFromOrganizer(user_db.email, db)

def get_all(offset: int, limit: int, db: Session):
    return event.getAll(offset, limit, db)

def check_permissions(user_db: Organizer, event_db: Event):
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    if user_db.email != event_db.organizer_email:
        raise HTTPException(status_code=404, detail="Permission denied.")