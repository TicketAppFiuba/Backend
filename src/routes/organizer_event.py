from fastapi import APIRouter, Depends
from src.config.db import get_db, engine
from sqlalchemy.orm import Session
from src.models import event, image
from src.models.organizer import Organizer
from src.schemas.event import *
from src.schemas.image import *
from src.controllers.organizer_access import verify
from src.controllers.event import create_event, update_event, delete_event, get_event, get_events_from

router = APIRouter(tags=["Events | Organizer"])
event.Base.metadata.create_all(bind=engine)

@router.post("/event/create", status_code=200)
def create(eventSchema: EventSchema, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return create_event(eventSchema, user_db, db)

@router.put("/event/update", status_code=200)
def update(eventSchema: EventSchemaUpdate, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return update_event(eventSchema, user_db, db)

@router.delete("/event/delete", status_code=200)
def delete(event_id: int, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return delete_event(event_id, user_db, db)

@router.get("/event/info", status_code=200)
def get(event_id: int, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return get_event(event_id, user_db, db)

@router.get("/organizer/events", status_code=200)
def get_events_from_organizer(user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return get_events_from(user_db, db)