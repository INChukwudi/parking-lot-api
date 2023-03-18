from pydantic import BaseModel


class OwnerBase(BaseModel):
    firstName: str
    lastName: str
    email: str
    gender: str
    dob: str
    passport: str
    qr_code: str


class OwnerCreate(OwnerBase):
    pass


class Owner(OwnerBase):
    id: int

    class Config:
        orm_mode = True
