from src.models.organizer import Organizer
from sqlalchemy.orm import Session
from src.schemas.user import UserSchema

def create(user: UserSchema, db: Session):
    user_db = Organizer(email=user.email, name=user.name, login=True)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def update(user_db: Organizer, new_attributes: dict(), db: Session):
    for attr, value in new_attributes.items():
        setattr(user_db, attr, value)
    db.commit()
    db.refresh(user_db)
    return user_db

def get(email: str, db: Session):
    return db.query(Organizer).filter(Organizer.email == email).first()
