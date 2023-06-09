from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class TopOrganizersByAttendancesSchemaOut(BaseModel):
    organizer_email: str
    attendances: int

    class Config:
        orm_mode = True

class TopOrganizersByNumberOfEventsSchemaOut(BaseModel):
    organizer_email: str
    amount: int

    class Config:
        orm_mode = True

class ComplaintsDistributionSchema(BaseModel):
    date: str
    complaints: int

    class Config:
        orm_mode = True

class SuspensionsDistributionSchema(BaseModel):
    date: str
    suspensions: int

    class Config:
        orm_mode = True

class EventsDistributionSchema(BaseModel):
    date: str
    events: int

    class Config:
        orm_mode = True

class AttendancesDistributionSchema(BaseModel):
    date: str
    attendances: int

    class Config:
        orm_mode = True

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
    category: Optional[str]
 
    class Config:
        orm_mode = True