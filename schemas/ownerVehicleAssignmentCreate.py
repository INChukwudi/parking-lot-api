from pydantic import BaseModel


class OwnerVehicleAssignmentCreate(BaseModel):
    vehicle_id: str
    owner_id: str
    centre_id: str
