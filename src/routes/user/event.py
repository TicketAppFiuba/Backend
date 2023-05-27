from fastapi import APIRouter, Depends
from src.config.db import get_db
from sqlalchemy.orm import Session
from src.controllers.user.access import verify
from src.models.user import User
from src.controllers.user import event
from src.schemas.query import QuerySchema
from src.schemas.event import *
from typing import List, Union

user_event = APIRouter(tags=["User | Events"])

@user_event.get("/user/event", response_model = EventUserSchemaOut, status_code=200)
def get_event(event_id: int, user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return event.get_event(event_id, db)

@user_event.get("/user/events", response_model=List[EventWithDistanceSchemaOut], status_code=200)
def get_events(title: Union[str, None] = None, 
               category: Union[str, None] = None, 
               direction: str  = "-", 
               latitude: float  = 0, 
               longitude: float = 0, 
               offset: int = 0, 
               limit: int = 100, 
               user_db: User = Depends(verify), 
               db: Session = Depends(get_db)):
    query = QuerySchema(title=title, 
                        category=category, 
                        ubication=UbicationSchema(direction=direction,
                                                  latitude=latitude,
                                                  longitude=longitude))
    return event.get_all_event(query, offset, limit, db)


