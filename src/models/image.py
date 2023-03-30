from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.config.db import Base

class Image(Base): 
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    link = Column(String, nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'), index=True)
    event = relationship("Event", back_populates="images")