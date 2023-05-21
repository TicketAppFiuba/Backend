from fastapi import APIRouter, Depends
from src.config.db import get_db
from sqlalchemy.orm import Session
from src.models.authorizer import Authorizer
from src.controllers.authorizer import attendances
from src.controllers.authorizer.access import verify
from src.schemas.attendance import AttendanceOutSchema
from typing import List

authorizer_attendances = APIRouter(tags=["Auhorizer | Attendances"])

@authorizer_attendances.get("/authorizer/event/attendances", response_model=List[AttendanceOutSchema], status_code=200)
def event_attendances(event_id: int, authorizer_db: Authorizer = Depends(verify), db: Session = Depends(get_db)):
    return attendances.get_attendances(event_id, authorizer_db, db) 

