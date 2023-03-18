from database.config import Base
from sqlalchemy import Column, Integer, String, Date


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False, index=True, unique=True)
    passport = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    qr_code = Column(String, default="")
    dob = Column(Date, nullable=False)

