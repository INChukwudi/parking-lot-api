from database.config import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    dob = Column(Date, nullable=False)

    vehicles = relationship("Vehicle", back_populates="owners")
