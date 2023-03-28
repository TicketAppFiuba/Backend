from models.user import User
from sqlalchemy.orm import Session

def create(username: str, db: Session):
    user_db = User(username=username, login=True)
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

def get(username: str, db: Session):
    return db.query(User).filter(User.username == username).first()