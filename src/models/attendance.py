from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Attendance(Base):
    __tablename__ = "attendances"
    id = Column(Integer, primary_key=True)
    reservation_id = Column(Integer, ForeignKey("reservations.id"), index=True)
    date = Column(Date)
    hour = Column(String)
    reservation = relationship("Reservation", back_populates="attendance")