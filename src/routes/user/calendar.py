from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.models.user import User
from src.controllers.user.access import verify
from src.controllers.user import calendar, event
from src.schemas.event import EventSchemaOut


user_calendar = APIRouter(tags=["User | Calendar"])

@user_calendar.post("/user/event/calendar", status_code=200)
def add_calendar(event_id: int, user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return calendar.add_calendar(event_id, user_db, db)

@user_calendar.delete("/user/event/calendar", status_code=200)
def delete_calendar(event_id: int, user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return calendar.delete_calendar(event_id, user_db, db)
    
@user_calendar.get("/user/calendar", status_code=200)
def get_calendar(user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return calendar.get_calendar(user_db, db)