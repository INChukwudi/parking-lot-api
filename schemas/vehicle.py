from pydantic import BaseModel

from schemas.owner import Owner


class VehicleBase(BaseModel):
    manufacturer: str
    model: str
    year: int
    numberPlate: str
    kind: str


class VehicleCreate(VehicleBase):
    centre_id: str
    owner_id: str


class Vehicle(VehicleBase):
    id: int
    centre_id: int

    class Config:
        orm_mode = True
