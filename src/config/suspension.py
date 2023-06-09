from sqlalchemy.orm import Session
from src.models.suspension import Suspension
from datetime import datetime

def create(db: Session):
    suspension_db = Suspension(date=datetime.now().date())
    db.add(suspension_db)
    db.commit()
    db.refresh(suspension_db)
    return suspension_db

