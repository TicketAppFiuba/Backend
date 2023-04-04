from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.organizer import Organizer
from src.models.event import Event
from src.schemas.event import EventSchema, EventSchemaUpdate, EventSchemaOut
from src.schemas.ubication import UbicationSchema
from src.config import event
from src.schemas.image import *
from src.schemas.query import QuerySchema

def create_event(eventSchema: EventSchema, user_db: Organizer, db: Session):
    event_db = event.create(eventSchema, user_db.email, db)
    return {"detail": "Event created successfully", "id": event_db.id}

def update_event(eventSchema: EventSchemaUpdate, user_db: Organizer, db: Session):
    event_db = event.get(eventSchema.id, db)
    check_permissions(user_db, event_db)
    event_dict = eventSchema.dict(exclude_unset=True, exclude_none=True, exclude={'id'})
    event.update(event_db, event_dict, db)
    return {"detail": "Event modified successfully."}

def delete_event(event_id: int, user_db: Organizer, db: Session):
    event_db = event.get(event_id, db)
    check_permissions(user_db, event_db)
    event.delete(event_db, db)
    return {"detail": "Event deleted successfully."}

def get_event(event_id: int, user_db: Organizer, db: Session):
    event_db = event.get(event_id, db)
    check_permissions(user_db, event_db)
    return create_message(event_db)

def get_events_from(user_db: Organizer, db: Session):
    return event.getAllEventFromOrganizer(user_db.email, db)

def get_all(query: QuerySchema, offset: int, limit: int, db: Session):
    return event.getAll(query, offset, limit, db)

def check_permissions(user_db: Organizer, event_db: Event):
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    if user_db.email != event_db.organizer_email:
        raise HTTPException(status_code=404, detail="Permission denied.")

def create_message(event_db: Event): #Como puedo optimizar esto?
    return EventSchemaOut(
        id=event_db.id,
        title=event_db.title,
        description=event_db.description,
        organizer=event_db.organizer_email,
        category=event_db.category,
        date=event_db.date,
        capacity=event_db.capacity,
        vacancies=event_db.vacancies,
        ubication=UbicationSchema(direction=event_db.direction,
                                  latitude=event_db.latitude,
                                  length=event_db.length)
    )