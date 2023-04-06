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

def update(faq_db: FAQ, faqSchema: FaqUpdateSchema, db: Session):
    faq_db.question = faqSchema.question
    faq_db.answer = faqSchema.answer
    db.commit()
    db.refresh(faq_db)
    return faq_d

def getAllFromEvent(event_id: int, db: Session):
    return db.query(FAQ).filter(Faq.event_id == event_id).all()
