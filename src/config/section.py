from src.models.section import Section
from sqlalchemy.orm import Session

def getAllFromEvent(event_id: int, db: Session):
    return db.query(Section).filter(Section.event_id == event_id).all()