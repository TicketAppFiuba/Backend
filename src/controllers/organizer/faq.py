from sqlalchemy.orm import Session
from src.models.organizer import Organizer
from src.config import event, faq
from src.schemas.faq import *
from src.controllers.organizer.validations import *

def add_faq_to_event(faqSchema: FAQSchema, user_db: Organizer, db: Session):
    check_event(faqSchema.event_id, user_db, db)
    faq_db = faq.create(faqSchema, db)
    return {"detail": "FAQ created successfully", "id": faq_db.id}

def update_faq_to_event(faqSchema: FAQUpdateSchema, user_db: Organizer, db: Session):
    faq_db = check_faq(faqSchema, user_db, db)
    faq_dict = faqSchema.dict(exclude_unset=True, exclude_none=True, exclude={'id'})
    faq.update(faq_db, faq_dict, db)
    return {"detail": "FAQ modified successfully."}

def delete_faq_to_event(faqSchema: FAQDeleteSchema, user_db: Organizer, db: Session):
    faq_db = check_faq(faqSchema, user_db, db)
    faq.delete(faq_db, db)
    return {"detail": "FAQ deleted successfully."}