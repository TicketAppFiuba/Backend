from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date, DateTime, Boolean
from sqlalchemy.orm import relationship
from . import Base

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    organizer_email = Column(String, ForeignKey("organizers.email"))
    description = Column(String)
    title = Column(String)
    category = Column(String)
    direction = Column(String)
    init_date = Column(DateTime)
    end_date = Column(DateTime)
    create_date = Column(DateTime)
    capacity = Column(Integer)
    vacancies = Column(Integer)  
    latitude = Column(Float)
    longitude = Column(Float)
    pic_id = Column(Integer)
    state = Column(String)
    notified = Column(Boolean, default=False)
    organizer = relationship("Organizer", back_populates="events")
    images = relationship('Image', back_populates="event", cascade="all, delete, delete-orphan")
    faqs = relationship('FAQ', back_populates="event", cascade="all, delete, delete-orphan")
    sections = relationship('Section', back_populates="event", cascade="all, delete, delete-orphan")
    reservations = relationship('Reservation', back_populates="event", cascade="all, delete, delete-orphan")
    authorizers = relationship('EventAuthorizer', back_populates="event", cascade="all, delete, delete-orphan")
    complaints = relationship('Complaint', back_populates="event", cascade="all, delete, delete-orphan")
    favorites = relationship('Favorite', back_populates="event", cascade="all, delete, delete-orphan")
    calendar = relationship('Calendar', back_populates="event", cascade="all, delete, delete-orphan")   
