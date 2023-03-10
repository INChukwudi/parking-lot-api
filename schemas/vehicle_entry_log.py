from pydantic import BaseModel
from pydantic.schema import datetime


class VehicleEntryLogBase(BaseModel):
    vehicle_id: int
    owner_id: int
    centre_id: int
    entry_date_time: datetime
    exit_date_time: datetime | None = None


class VehicleEntryLogCreate(VehicleEntryLogBase):
    pass


class VehicleEntryLog(VehicleEntryLogBase):
    id: int

    class Config:
        orm_mode = True
