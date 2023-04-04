from sqlalchemy.orm import Session
from src.schemas.faq import *
from src.models.faq import Faq

def create(faq: FaqSchema, db: Session):
    faq_db = Faq(question=faq.question, answer=faq.answer, event_id=faq.event_id)
    db.add(faq_db)
    db.commit()
    db.refresh(faq_db)
    return faq_db

def update(faq_db: Faq, faqSchema: FaqUpdateSchema, db: Session):
    faq_db.question = faqSchema.question
    faq_db.answer = faqSchema.answer
    db.commit()
    db.refresh(faq_db)
    return faq_db

def delete(faq_db: Faq, db: Session):
    db.delete(faq_db)
    db.commit()

def get(faq_id: int, db: Session):
    return db.query(Faq).filter(Faq.id == faq_id).first()

def getAllFromEvent(event_id: int, db: Session):
    return db.query(Faq).filter(Faq.event_id == event_id).all()