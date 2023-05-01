from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Complaint(Base):
    __tablename__ = "complaints"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    category = Column(String)
    description = Column(String)
    event = relationship("Event", back_populates="complaints")
    user = relationship("User", back_populates="complaints")