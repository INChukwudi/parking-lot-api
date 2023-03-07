from pydantic import BaseModel


class AdminBase(BaseModel):
    firstName: str
    lastName: str
    email: str
    centreId: int
    level: int


class AdminCreate(AdminBase):
    password: str
    centre_id: str


class Admin(AdminBase):
    id: int
    centre_id: int

    class Config:
        orm_mode = True
