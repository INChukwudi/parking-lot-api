from database.config import Base
from datetime import date
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship


class Centre(Base):
    __tablename__ = "centres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    address = Column(String, nullable=False, index=True)
    capacity = Column(Integer, nullable=False)
    created_at = Column(Date, nullable=False, default=date.today())

    admins = relationship("Admin", back_populates="centre")
    assignments = relationship("OwnerVehicleAssignment", back_populates="centre")
