from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.schemas.complaint import *
from src.config.complaint import *
from src.controllers.admin import complaint
from src.controllers.admin.access import verify
from src.schemas.event import *

adm_complaint = APIRouter(tags=["Admin | Complaints"])

@adm_complaint.get("/admin/complaints", status_code=200)
def complaints(category: str | None = None,
               admin: str = Depends(verify), 
               db: Session = Depends(get_db)):
    query = ComplaintQuerySchema(category=category)
    return complaint.get_complaints(query, db)

@adm_complaint.get("/admin/event/complaints", status_code=200)
def complaints_by_event(event_id: int, admin: str = Depends(verify), db: Session = Depends(get_db)):
    return complaint.get_complaints_by_event(event_id, db)

@adm_complaint.get("/admin/user/complaints", status_code=200)
def complaints_by_user(email: str, admin: str = Depends(verify), db: Session = Depends(get_db)):
    return complaint.get_complaints_by_user(email, db)

@adm_complaint.get("/admin/complaints/categorys", status_code=200)
def categorys(admin: str = Depends(verify), db: Session = Depends(get_db)):
    return complaint.get_categorys(db)