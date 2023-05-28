from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from . import Base

class Calendar(Base):
    __tablename__ = "calendar"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    event_id = Column(Integer, ForeignKey('events.id'), index=True)
    user = relationship("User", back_populates="calendar")   
    event = relationship("Event", back_populates="calendar")    
