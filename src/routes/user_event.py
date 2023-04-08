from fastapi import APIRouter, Depends
from src.config.db import get_db
from sqlalchemy.orm import Session
from src.models import event
from src.controllers.user_access import verify
from src.models.user import User
from src.controllers import event
from src.schemas.query import QuerySchema

router = APIRouter(tags=["Events | User"])

@router.post("/events", status_code=200)
def get_events(query: QuerySchema, offset: int = 0, limit: int = 15, user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return event.getAll(query, offset, limit, db)

@router.get("/event", status_code=200)
def get_event(event_id: int, user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return event.getEvent(event_id, db)