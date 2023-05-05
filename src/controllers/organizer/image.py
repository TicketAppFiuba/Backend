from sqlalchemy.orm import Session
from src.models.organizer import Organizer
from src.config import event, image
from src.schemas.image import *
from src.controllers.organizer.permissions import *

def add_image_to_event(imageSchema: ImageSchema, user_db: Organizer, db: Session):
    check_event(imageSchema.event_id, user_db, db)
    image_db = image.create(imageSchema, db)
    return {"detail": "Image created successfully", "id": image_db.id}

def update_image_to_event(imageSchema: ImageUpdateSchema, user_db: Organizer, db: Session):
    image_db = check_img(imageSchema, user_db, db)
    image.update(image_db, imageSchema, db)
    return {"detail": "Image modified successfully."}

def delete_image_to_event(imageSchema: ImageDeleteSchema, user_db: Organizer, db: Session):
    image_db = check_img(imageSchema, user_db, db)
    image.delete(image_db, db)
    return {"detail": "Image deleted successfully."}

def get_all_images_to_event(event_id: int, user_db: Organizer, db: Session):
    check_event(event_id, user_db, db)
    return image.getAllFromEvent(event_id, db)

def add_event_cover_pic(imageSchema: ImageSchema, user_db: Organizer, db: Session):
    event_db = check_event(imageSchema.event_id, user_db, db)
    image_db = image.getImageBy(imageSchema, db)
    if image_db is None:
        image_db = image.create(imageSchema, db)
    event.change_pic(event_db, image_db.id, db)
    return {"detail": "The cover image has been updated."}