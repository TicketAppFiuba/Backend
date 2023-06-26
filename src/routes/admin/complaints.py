from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.schemas.complaint import *
from src.config.complaint import *
from src.controllers.admin import complaint
from src.controllers.admin.access import verify
from src.schemas.event import *
from typing import Union

adm_complaint = APIRouter(tags=["Admin | Complaints"])

@adm_complaint.get("/admin/complaints", status_code=200)
def complaints(category: Union[str, None] = None,
               date_init: Union[date, None] = None,
               date_end: Union[date, None] = None,
               admin: str = Depends(verify), 
               db: Session = Depends(get_db)):
    query = ComplaintQuerySchema(category=category, date_init=date_init, date_end=date_end)
    return complaint.get_complaints(query, db)
    
@adm_complaint.get("/admin/complaintsUsers", status_code=200)
def complaints(category: Union[str, None] = None,
               date_init: Union[date, None] = None,
               date_end: Union[date, None] = None,
               admin: str = Depends(verify), 
               db: Session = Depends(get_db)):
    query = ComplaintQuerySchema(category=category, date_init=date_init, date_end=date_end)
    return complaint.get_complaints_users(query, db)    

@adm_complaint.get("/admin/event/complaints", status_code=200)
def complaints_by_event(event_id: int, admin: str = Depends(verify), db: Session = Depends(get_db)):
    return complaint.get_complaints_by_event(event_id, db)

@adm_complaint.get("/admin/user/complaints", status_code=200, response_model=List[ComplaintPerUserSchema])
def complaints_by_user(email: str, admin: str = Depends(verify), db: Session = Depends(get_db)):
    return complaint.get_complaints_by_user(email, db)

@adm_complaint.get("/admin/complaints/categorys", status_code=200)
def categorys(admin: str = Depends(verify), db: Session = Depends(get_db)):
    return complaint.get_categorys(db)
