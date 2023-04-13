from fastapi import APIRouter, Depends
from src.config.db import get_db, engine
from sqlalchemy.orm import Session
from src.models.organizer import Organizer
from src.models import image
from src.schemas.event import *
from src.schemas.image import *
from src.controllers.organizer.access import verify
from src.controllers.organizer.image import add_image_to_event, update_image_to_event, delete_image_to_event, get_all_images_to_event

router = APIRouter(tags=["Event Images | Organizer"])
image.Base.metadata.create_all(bind=engine)

@router.post("/organizer/event/images", status_code=200)
def add(image: ImageSchema, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return add_image_to_event(image, user_db, db)

@router.put("/organizer/event/images", status_code=200)
def update(image: ImageUpdateSchema, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return update_image_to_event(image, user_db, db)

@router.delete("/organizer/event/images", status_code=200)
def delete(image: ImageDeleteSchema, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return delete_image_to_event(image, user_db, db)

@router.get("/organizer/event/images", status_code=200)
def get(event_id: int, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return get_all_images_to_event(event_id, user_db, db)