from database.config import Base
from sqlalchemy import Column, Integer, Boolean


class OwnerVehicleAssignment(Base):
    __tablename__ = "ownerVehicleAssignments"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, nullable=False)
    vehicle_id = Column(Integer, nullable=False)
    centre_id = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
