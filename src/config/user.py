from src.models.user import User
from sqlalchemy.orm import Session
from src.schemas.user import UserSchema

def create(user: UserSchema, db: Session):
    user_db = User(email=user.email, name=user.name, login=True, suspended=False)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def update(user_db: User, new_attributes: dict(), db: Session):
    for attr, value in new_attributes.items():
        setattr(user_db, attr, value)
    db.commit()
    db.refresh(user_db)
    return user_db

def suspend(user_db, db: Session):
    user_db.suspended = True
    db.commit()
    db.refresh(user_db)

def get(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()
