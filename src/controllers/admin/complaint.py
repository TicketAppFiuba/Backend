from sqlalchemy.orm import Session
from src.config import complaint
from src.schemas.complaint import *

def get_complaints(query: ComplaintQuerySchema, db: Session):
    return complaint.getAll(query, db)