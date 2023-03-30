from sqlalchemy import Column, Integer, String, Boolean
from src.config.db import Base

class Organizer(Base):
    __tablename__ = "organizers"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    login = Column(Boolean)
