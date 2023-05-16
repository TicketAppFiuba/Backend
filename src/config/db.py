from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base
from src.models.event import Event
from src.models.faq import FAQ
from src.models.image import Image
from src.models.organizer import Organizer
from src.models.user import User
from src.models.reservation import Reservation
from src.models.section import Section
from src.models.authorizer import Authorizer
from src.models.event_authorizer import EventAuthorizer
from src.models.complaint import Complaint
from src.models.favorites import Favorite

engine = create_engine("sqlite:///./sql_app.db", connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)
