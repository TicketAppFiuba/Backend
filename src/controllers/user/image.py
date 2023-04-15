from sqlalchemy.orm import Session
from src.config import image
from src.schemas.image import *
from src.controllers.user.validations import *

def get_all_images_from_event(event_id: int, db: Session):
    validate_event(event_id, db)
    return image.getAllFromEvent(event_id, db)