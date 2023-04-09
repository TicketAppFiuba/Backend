from fastapi import APIRouter, Depends
from src.config.db import get_db
from sqlalchemy.orm import Session
from src.models import event
from src.controllers.user.access import verify
from src.models.user import User
from src.controllers.user import event
from src.schemas.query import QuerySchema
from src.schemas.event import *
from typing import List

router = APIRouter(tags=["Events | User"])

@router.get("/user/events", response_model = List[EventSchemaOut], status_code=200)
def get_events(title: str | None = None, 
               category: str | None = None, 
               direction: str  = "-", 
               latitude: int  = 0, 
               longitude: int = 0, 
               offset: int = 0, 
               limit: int = 15, 
               user_db: User = Depends(verify), 
               db: Session = Depends(get_db)):
    query = QuerySchema(title=title, 
                        category=category, 
                        ubication=UbicationSchema(direction=direction,
                                                  latitude=latitude,
                                                  length=longitude))
    return event.get_all_event(query, offset, limit, db)

@router.get("/user/event", response_model = EventAllInfoSchemaOut, status_code=200)
def get_event(event_id: int, user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return event.get_event(event_id, db)