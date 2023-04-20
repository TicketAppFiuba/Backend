from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class EventAuthorizer(Base):
    __tablename__ = "eventsauthorizers"
    id = Column(Integer, primary_key=True)
    email = Column(String, ForeignKey('authorizers.email'), index=True)
    event_id = Column(Integer, ForeignKey('events.id'), index=True)
    authorizer = relationship("Authorizer", back_populates="events")
    event = relationship("Event", back_populates="authorizers")
