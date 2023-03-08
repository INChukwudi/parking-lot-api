from database.config import Base
from sqlalchemy import Column, Integer, Boolean, ForeignKey


class OwnerVehicleAssignment(Base):
    __tablename__ = "ownerVehicleAssignments"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("owners.id"), nullable=False,)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    centre_id = Column(Integer, ForeignKey("centres.id"), nullable=False)
    is_active = Column(Boolean, default=True)
