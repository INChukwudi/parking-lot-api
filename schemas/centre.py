from pydantic import BaseModel
from schemas.admin import Admin
from schemas.vehicle import Vehicle


class CentreBase(BaseModel):
    name: str
    address: str
    capacity: int


class CentreCreate(CentreBase):
    pass


class Centre(CentreBase):
    id: int
    admins: list[Admin] = []
    vehicles: list[Vehicle] = []

    class Config:
        orm_mode = True
