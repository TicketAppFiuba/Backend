from pydantic import BaseModel
from typing import List

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