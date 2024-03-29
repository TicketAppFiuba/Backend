from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from . import Base

class Reservation(Base): 
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    tickets = Column(Integer)
    code = Column(String)
    scanned = Column(Boolean)
    user = relationship("User", back_populates="reservations")   
    event = relationship("Event", back_populates="reservations")
    attendance = relationship("Attendance", back_populates="reservation")
