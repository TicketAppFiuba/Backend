from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.schemas.complaint import *
from src.config.complaint import *
from src.controllers.admin import moderation
from src.controllers.admin.access import verify

adm_moderation = APIRouter(tags=["Admin | Moderation"])

@adm_moderation.post("/admin/user/suspend", status_code=200)
def suspend_user(email: str, admin: str = Depends(verify), db: Session = Depends(get_db)):
    return moderation.suspend_user(email, db)

@adm_moderation.post("/admin/event/suspend", status_code=200)
def suspend_event(event_id: int, admin: str = Depends(verify), db: Session = Depends(get_db)):
    return moderation.suspend_event(event_id, db)

@adm_moderation.post("/admin/user/enable", status_code=200)
def enabled_user(email: str, admin: str = Depends(verify), db: Session = Depends(get_db)):
    return moderation.enabled_user(email, db)

@adm_moderation.post("/admin/event/enable", status_code=200)
def enable_event(event_id: int, admin: str = Depends(verify), db: Session = Depends(get_db)):
    return moderation.enable_event(event_id, db)

@adm_moderation.get("/admin/complaints", status_code=200)
def complaints(admin: str = Depends(verify), db: Session = Depends(get_db)):
    return getAll(db)
