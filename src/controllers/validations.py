from fastapi import HTTPException
from src.models.user import User
from src.models.organizer import Organizer
from src.models.event import Event
from src.models.image import Image
from src.models.faq import FAQ
from src.schemas.image import *
from src.config.reservation import *

def check_permissions(user_db: Organizer, event_db: Event):
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    if user_db.email != event_db.organizer_email:
        raise HTTPException(status_code=404, detail="Permission denied.")

def check_permission_img(image_db: Image, event_db: Event):
    if image_db is None:
        raise HTTPException(status_code=404, detail="Image not exist.")
    if image_db.event_id != event_db.id:
        raise HTTPException(status_code=404, detail="Not permission.")
        
def check_permission_faq(faq_db: FAQ, event_db: Event):
    if faq_db is None:
        raise HTTPException(status_code=404, detail="FAQ not exist.")
    if faq_db.event_id != event_db.id:
        raise HTTPException(status_code=404, detail="Not permission.")
    
def check_event_exist(event_db: Event):
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")

def check_permission_reservation(user_db: User, event_db: Event, db: Session):
    check_event_exist(event_db)
    reservation_db = getByUserAndEvent(user_db.id, event_db.id, db)
    if reservation_db is not None:
        raise HTTPException(status_code=404, detail="Not permission.")
