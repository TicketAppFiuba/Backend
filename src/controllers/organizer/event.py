from sqlalchemy.orm import Session
from src.models.organizer import Organizer
from src.schemas.event import EventSchema, EventSchemaUpdate
from src.config import event
from src.schemas.image import *
from src.controllers.organizer.validations import *

def create_event(eventSchema: EventSchema, user_db: Organizer, db: Session):
    event_db = event.create(eventSchema, user_db.email, db)
    return {"detail": "Event created successfully", "id": event_db.id}

def update_event(eventSchema: EventSchemaUpdate, user_db: Organizer, db: Session):
    event_db = check_event(eventSchema.id, user_db, db)
    event_dict = eventSchema.dict(exclude_unset=True, exclude_none=True, exclude={'id'})
    event_agenda = event_dict.pop('agenda', [])
    event.update(event_db, event_dict, db, event_agenda)
    return {"detail": "Event modified successfully."}

def delete_event(event_id: int, user_db: Organizer, db: Session):
    event_db = check_event(event_id, user_db, db)
    event.delete(event_db, db)
    return {"detail": "Event deleted successfully."}

def get_event(event_id: int, user_db: Organizer, db: Session):
    event_db = check_event(event_id, user_db, db)
    return event_db

def get_events_from(user_db: Organizer, db: Session):
    return event.getAllEventFromOrganizer(user_db.email, db)
