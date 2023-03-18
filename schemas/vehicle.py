from pydantic import BaseModel


class VehicleBase(BaseModel):
    manufacturer: str
    model: str
    year: int
    number_plate: str


class VehicleCreate(VehicleBase):
    owner_id: int
    centre_id: int


class Vehicle(VehicleBase):
    id: int
    # centre_id: int

    class Config:
        orm_mode = True
