from fastapi import APIRouter, Depends
from src.config.db import get_db, engine
from sqlalchemy.orm import Session
from src.models import image
from src.models.organizer import Organizer
from src.schemas.event import *
from src.schemas.image import *
from src.controllers.organizer_access import verify
from src.controllers.image import add_image_to_event, update_image_to_event

router = APIRouter(tags=["Event Images"])
image.Base.metadata.create_all(bind=engine)

@router.post("/event/images/add", status_code=200)
def add_image(image: ImageSchema, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return add_image_to_event(image, user_db, db)

@router.put("/event/images/update", status_code=200)
def update_image(image: ImageUpdateSchema, user_db: Organizer = Depends(verify), db: Session = Depends(get_db)):
    return update_image_to_event(image, user_db, db)