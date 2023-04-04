from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from src.config.db import Base

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    organizer_email = Column(String, ForeignKey("organizers.email"))
    description = Column(String)
    capacity = Column(Integer)
    vacancies = Column(Integer)  
    date = Column(Date)
    title = Column(String)
    category = Column(String)
    direction = Column(String)
    latitude = Column(String)
    length = Column(String)
    organizer = relationship("Organizer", back_populates="events")
    images = relationship('Image', back_populates="event", cascade="all, delete, delete-orphan")

