from sqlalchemy.orm import Session
from src.schemas.complaint import *
from src.controllers.user import validations
from src.config import complaint
from src.models.user import User

def create_complaint(complaintSchema: ComplaintCreateSchema, user_db: User, db: Session):
    complaintSchema = validations.check_permission_complaint(complaintSchema, user_db, db)
    complaint_db = complaint.create(complaintSchema, db)
    return {"detail": "Complaint created successfully", "id": complaint_db.id}

def get_complaints_from_user(user_db: User, db: Session):
    return complaint.getAllFromUser(user_db.id, db)