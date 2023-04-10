from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.organizer import Organizer
from src.models.event import Event
from src.models.image import Image
from src.config import event, image
from src.schemas.image import *

def add_image_to_event(imageSchema: ImageSchema, user_db: Organizer, db: Session):
    event_db = event.get(imageSchema.event_id, db)
    check_permissions(user_db, event_db)
    image_db = image.create(imageSchema, db)
    return {"detail": "Image created successfully", "id": image_db.id}

def update_image_to_event(imageSchema: ImageUpdateSchema, user_db: Organizer, db: Session):
    event_db = event.get(imageSchema.event_id, db)
    check_permissions(user_db, event_db)
    image_db = image.get(imageSchema.id, db)
    check_permission_img(image_db, event_db)
    image.update(image_db, imageSchema, db)
    return {"detail": "Image modified successfully."}

def delete_image_to_event(imageSchema: ImageDeleteSchema, user_db: Organizer, db: Session):
    event_db = event.get(imageSchema.event_id, db)
    check_permissions(user_db, event_db)
    image_db = image.get(imageSchema.id, db)
    check_permission_img(image_db, event_db)
    image.delete(image_db, db)
    return {"detail": "Image deleted successfully."}

def get_all_images_to_event(event_id: int, user_db: Organizer, db: Session):
    event_db = event.get(event_id, db)
    check_permissions(user_db, event_db)
    return image.getAllFromEvent(event_id, db)

def check_permission_img(image_db: Image, event_db: Event):
    if image_db is None:
        raise HTTPException(status_code=404, detail="Image not exist.")
    if image_db.event_id != event_db.id:
        raise HTTPException(status_code=404, detail="Not permission.")
    
def check_permissions(user_db: Organizer, event_db: Event):
    if event_db is None:
        raise HTTPException(status_code=404, detail="Event not exist.")
    if user_db.email != event_db.organizer_email:
        raise HTTPException(status_code=404, detail="Permission denied.")