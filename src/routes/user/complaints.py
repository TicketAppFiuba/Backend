from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.schemas.complaint import *
from src.controllers.user.access import verify
from src.controllers.user.complaint import *
from src.models.user import User

user_complaints = APIRouter(tags=["User | Complaints"])

@user_complaints.post("/user/event/complaint", status_code=200)
def report(complaintSchema: ComplaintCreateSchema, user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return create_complaint(complaintSchema, user_db, db)

@user_complaints.get("/user/complaints", status_code=200)
def complaint(user_db: User = Depends(verify), db: Session = Depends(get_db)):
    return get_complaints_from_user(user_db, db)

from src.config.complaint import *
@user_complaints.get("/complaints/users/ranking", status_code=200)
def complaint(db: Session = Depends(get_db)):
    return getRankingFromUsers(db)

@user_complaints.get("/complaints/events/ranking", status_code=200)
def complaint(db: Session = Depends(get_db)):
    return getRankingFromEvents(db)
