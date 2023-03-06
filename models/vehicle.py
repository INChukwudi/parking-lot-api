from database.config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    manufacturer = Column(String, nullable=False, index=True)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    number_plate = Column(String, nullable=False, index=True)

    owners = relationship("Owner", back_populates="vehicles")
    centre = relationship("Centre", back_populates="vehicles")
