from fastapi import APIRouter, Depends
from src.config.db import get_db, engine
from sqlalchemy.orm import Session
from src.schemas.event import *
from src.schemas.faq import FAQSchema, FAQDeleteSchema
from src.controllers.organizer_access import verify
from src.models.organizer import Organizer
from src.controllers.faq import *
from src.models import faq

router = APIRouter(tags=["Event FAQ | Organizer"])
faq.Base.metadata.create_all(bind=engine)

@router.post("/event/faq/add", status_code=200)
def add(faqSchema: FAQSchema, organizer: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return add_faq_to_event(faqSchema, organizer, db)

#@router.put("/event/question/update", status_code=200)
#def update(db: Session = Depends(get_db)):
#    return 1

@router.delete("/event/faq/delete", status_code=200)
def delete(faqSchema: FAQDeleteSchema, organizer: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return delete_faq_to_event(faqSchema, organizer, db)

#@router.get("/event/faq", status_code=200)
#def get(db: Session = Depends(get_db)):
#    return 1