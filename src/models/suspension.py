from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from . import Base

class Suspension(Base):
    __tablename__ = "suspensions"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
