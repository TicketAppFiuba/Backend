from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.organizer import Organizer
from src.config import event, image
from src.schemas.image import *
from src.controllers.event import check_permissions

def add_image_to_event(imageSchema: ImageSchema, user_db: Organizer, db: Session):
    event_db = event.get(imageSchema.event_id, db)
    check_permissions(user_db, event_db)
    image_db = image.create(imageSchema, db)
    return image_db

def update_image_to_event(imageSchema: ImageUpdateSchema, user_db: Organizer, db: Session):
    event_db = event.get(imageSchema.event_id, db)
    check_permissions(user_db, event_db)
    image_db = image.get(imageSchema.id, db)
    if image_db is None:
        raise HTTPException(status_code=404, detail="Image not exist.")
    return image.update(image_db, imageSchema, db)
