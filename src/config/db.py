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
#import os
#from dotenv import load_dotenv

#load_dotenv()

#db_hostname = os.environ["DATABASE_HOSTNAME"]
#db_port = os.environ["DATABASE_PORT"]
#database = os.environ["DATABASE"]
#db_username = os.environ["DATABASE_USERNAME"]
#db_password = os.environ["DATABASE_PASSWORD"]

#db_url="postgresql://{0}:{1}@{2}:{3}/{4}".format(db_username, db_password, db_hostname, db_port, database)

#engine = create_engine(db_url, pool_pre_ping=True)
engine = create_engine("sqlite:///./sql_app.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

