from sqlalchemy.orm import Session
from src.config import image
from src.schemas.image import *
from src.controllers.validator import validator

def get_all_images_from_event(event_id: int, db: Session):
    validator.validate_user_get_event(event_id, db)
    return image.getAllFromEvent(event_id, db)