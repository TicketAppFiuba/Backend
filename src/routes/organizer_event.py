from fastapi import APIRouter, Depends
from src.config.db import get_db, engine
from sqlalchemy.orm import Session
from src.models.organizer import Organizer
from src.schemas.event import *
from src.schemas.image import *
from src.controllers.organizer.access import verify
from src.controllers.organizer.event import create_event, update_event, delete_event, get_event, get_events_from

router = APIRouter(tags=["Events | Organizer"])

@router.post("/organizer/event", status_code=200)
def create(eventSchema: EventSchema, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return create_event(eventSchema, user_db, db)

@router.put("/organizer/event", status_code=200)
def update(eventSchema: EventSchemaUpdate, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return update_event(eventSchema, user_db, db)

@router.delete("/organizer/event", status_code=200)
def delete(event_id: int, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return delete_event(event_id, user_db, db)

@router.get("/organizer/event", status_code=200)
def get(event_id: int, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return get_event(event_id, user_db, db)

@router.get("/organizer/events", status_code=200)
def get_events_from_organizer(user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return get_events_from(user_db, db)

from sqlalchemy import text
@router.delete('/deleteDataBase/')
def delete():
    with engine.connect() as c:
        c.execute(text("DROP TABLE users"))
        c.execute(text("DROP TABLE organizers"))
        c.execute(text("DROP TABLE events"))
        c.execute(text("DROP TABLE images"))
        c.execute(text("DROP TABLE faqs"))
        c.execute(text("DROP TABLE authorizers"))