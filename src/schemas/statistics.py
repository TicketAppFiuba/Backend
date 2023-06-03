from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class ReservationDateSchema(BaseModel):
    capacity: int
    vacancies: int
    occupancy: int
    reservation_ratio: float

    class Config:
        orm_mode = True

class AttendanceDateSchema(BaseModel):
    attendances: int
    availability: int
    attendance_ratio: float

    class Config:
        orm_mode = True

class AttendancePerHourSchema(BaseModel):
    hour: str
    attendances: int

    class Config:
        orm_mode = True

class StatisticsSchema(BaseModel):
    reservation_date: ReservationDateSchema
    attendance_date: AttendanceDateSchema
    distribution_per_hour: List[AttendancePerHourSchema]

    class Config:
        orm_mode = True

class QueryDistributionSchema(BaseModel):
    init_date: Optional[date]
    end_date: Optional[date]
 
    class Config:
        orm_mode = True