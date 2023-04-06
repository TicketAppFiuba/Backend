from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from src.config.db import Base

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    organizer_email = Column(String, ForeignKey("organizers.email"))
    description = Column(String)
    title = Column(String)
    category = Column(String)
    direction = Column(String)
    date = Column(Date)
    capacity = Column(Integer)
    vacancies = Column(Integer)  
    latitude = Column(Integer)
    length = Column(Integer)
    organizer = relationship("Organizer", back_populates="events")
    images = relationship('Image', back_populates="event", cascade="all, delete, delete-orphan")
    faq = relationship('FAQ', back_populates="event", cascade="all, delete, delete-orphan")

