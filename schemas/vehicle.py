from pydantic import BaseModel

from schemas.owner import Owner


class VehicleBase(BaseModel):
    manufacturer: str
    model: str
    year: int
    numberPlate: str
    kind: str


class VehicleCreate(VehicleBase):
    pass


class Vehicle(VehicleBase):
    id: int
    centre_id: int
    owners: list[Owner] = []

    class Config:
        orm_mode = True
