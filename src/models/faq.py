from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.config.db import Base

class FAQ(Base):
    __tablename__ = "faqs"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    response = Column(String)
    event_id = Column(Integer, ForeignKey('events.id'), index=True)
    event = relationship("Event", back_populates="faq")