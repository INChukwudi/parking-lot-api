from pydantic import BaseModel


class AdminBase(BaseModel):
    firstName: str
    lastName: str
    email: str
    level: int


class AdminCreate(AdminBase):
    password: str
    centre_id: int | None = None


class Admin(AdminBase):
    id: int
    centre_id: int

    class Config:
        orm_mode = True
