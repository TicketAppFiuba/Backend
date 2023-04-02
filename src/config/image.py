from sqlalchemy.orm import Session
from src.schemas.image import *
from src.models.image import Image

def create(image: ImageSchema, db: Session):
    image_db = Image(link=image.link, event_id=image.event_id)
    db.add(image_db)
    db.commit()
    db.refresh(image_db)
    return image_db

def update(image_db: Image, imageSchema: ImageUpdateSchema, db: Session):
    image_db.link = imageSchema.link
    db.commit()
    db.refresh(image_db)
    return image_db

def delete(image_db: Image, db: Session):
    db.delete(image_db)
    db.commit()

def get(image_id: int, db: Session):
    return db.query(Image).filter(Image.id == image_id).first()

def getAllFromEvent(event_id: int, db: Session):
    return db.query(Image).filter(Image.event_id == event_id).all()