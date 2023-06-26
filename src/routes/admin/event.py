from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.schemas.complaint import *
from src.config.complaint import *
from src.controllers.admin.access import verify
from src.schemas.event import *
from src.controllers.admin import event

adm_event = APIRouter(tags=["Admin | Event"])

@adm_event.get("/admin/event", response_model = EventAdminSchemaOut, status_code=200)
def get_event(event_id: int, admin: str = Depends(verify), db: Session = Depends(get_db)):
    return event.get_event(event_id, db)