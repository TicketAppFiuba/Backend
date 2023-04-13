from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from . import Base

class FAQ(Base):
    __tablename__ = "faqs"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    response = Column(String)
    event_id = Column(Integer, ForeignKey('events.id'), index=True)
    event = relationship("Event", back_populates="faq")
