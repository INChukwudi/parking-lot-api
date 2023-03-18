from pydantic import BaseModel


class OwnerVehicleAssignmentBase(BaseModel):
    vehicle_id: str
    owner_id: str
    centre_id: str


class OwnerVehicleAssignmentCreate(OwnerVehicleAssignmentBase):
    pass


class OwnerVehicleAssignment(OwnerVehicleAssignmentBase):
    class Config:
        orm_mode = True
