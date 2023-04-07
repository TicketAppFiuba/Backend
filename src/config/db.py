from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


#load_dotenv()

#db_hostname = os.environ["DATABASE_HOSTNAME"]
#db_port = os.environ["DATABASE_PORT"]
#database = os.environ["DATABASE"]
#db_username = os.environ["DATABASE_USERNAME"]
#db_password = os.environ["DATABASE_PASSWORD"]

#url="postgresql://{0}:{1}@{2}:{3}/{4}".format(db_username, db_password, db_hostname, db_port, database)

#engine = create_engine(url)
engine = create_engine("sqlite:///./sql_app.db", connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
