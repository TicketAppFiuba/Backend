from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from . import Base

class Authorizer(Base):
    __tablename__ = "authorizers"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    login = Column(Boolean)
