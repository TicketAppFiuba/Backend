from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Reservation(Base): 
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), index=True)
    event = relationship("Event", back_populates="reservations")
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    user = relationship("User", back_populates="reservations")   