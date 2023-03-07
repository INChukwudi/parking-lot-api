from pydantic import BaseModel
from schemas.vehicle import Vehicle


class OwnerBase(BaseModel):
    firstName: str
    lastName: str
    email: str
    gender: str
    dob: str
    passport: str
    qr_code: str


class OwnerCreate(OwnerBase):
    password: str


class Owner(OwnerBase):
    id: int
    vehicles: list[Vehicle] = []

    class Config:
        orm_mode = True
