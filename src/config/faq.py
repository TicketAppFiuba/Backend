from sqlalchemy.orm import Session
from src.schemas.faq import FAQSchema
from src.models.faq import FAQ

def create(faq: FAQSchema, db: Session):
    faq_db = FAQ(**faq.dict())
    db.add(faq_db)
    db.commit()
    db.refresh(faq_db)
    return faq_db

def delete(faq: FAQ, db: Session):
    db.delete(faq)
    db.commit()

def get(question_id: int, db: Session):
    return db.query(FAQ).filter(FAQ.id == question_id).first()