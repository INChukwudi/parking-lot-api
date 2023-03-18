from datetime import datetime, date
from typing import Union

from pydantic import BaseModel


class OwnerBase(BaseModel):
    firstName: str
    lastName: str
    email: str
    gender: str
    dob: Union[str | date]
    passport: str
    qr_code: str


class OwnerCreate(OwnerBase):
    pass


class Owner(OwnerBase):
    id: int

    class Config:
        orm_mode = True
