from fastapi import APIRouter, Depends
from src.config.db import get_db
from sqlalchemy.orm import Session
from src.controllers.user.access import verify
from src.models.user import User
from src.schemas.complaint import *

user_complaints = APIRouter(tags=["User | Complaints"])

@user_complaints.post("/user/event/complaint", status_code=200)
def report(complaint: ComplaintSchema, user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return 1

@user_complaints.get("/user/complaints", status_code=200)
def complaints(user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return 1


