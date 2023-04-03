from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

db_url = os.environ.get('DATABASE_URL')
db_port = os.environ.get('DATABASE_PORT')
database = os.environ.get('DATABASE')
db_username = os.environ.get('DATABASE_USERNAME')
db_password = os.environ.get('DATABASE_PASSWORD')

engine = create_engine(url="postgresql://{0}:{1}@{2}:{3}/{4}".format(db_username, db_password, db_url, db_port, database))

#engine = create_engine("sqlite:///./sql_app.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
