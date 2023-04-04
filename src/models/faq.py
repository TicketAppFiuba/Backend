from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from src.config.db import Base

class Faq(Base):
    __tablename__ = "faqs"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    question = Column(String)
    answer = Column(Integer)
