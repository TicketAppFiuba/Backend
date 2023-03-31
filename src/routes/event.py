from fastapi import APIRouter, Depends, HTTPException
from src.config.db import get_db, engine
from sqlalchemy.orm import Session
from src.models import event, image
from src.models.organizer import Organizer
from src.schemas.event import EventSchema, EventSchemaOut
from src.config.event import create, get, delete
from src.controllers.organizer_access import verify

router = APIRouter(tags=["Events"])
event.Base.metadata.create_all(bind=engine)
image.Base.metadata.create_all(bind=engine)

@router.post("/event/create", status_code=200)
def create_event(eventSchema: EventSchema, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return create(eventSchema, user_db.email, db)

@router.delete("/event/delete", status_code=200)
def delete_event(event_id: int, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    event_db = get(event_id, db)
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    if user_db.email != event_db.organizer_email:
        raise HTTPException(status_code=404, detail="Permission denied.")
    delete(event_db, db)
    return {"detail": "OK"}