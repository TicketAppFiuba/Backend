from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from . import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    login = Column(Boolean)
    reservations = relationship('Reservation', back_populates="user", cascade="all, delete, delete-orphan")
    complaints = relationship('Complaint', back_populates="user", cascade="all, delete, delete-orphan")
