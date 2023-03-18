from models.owner_vehicle_assignment import OwnerVehicleAssignment
from models.vehicle import Vehicle
from sqlalchemy.orm import Session

from schemas.owner_vehicle_assignment import OwnerVehicleAssignmentCreate
from schemas.vehicle import VehicleCreate


def find_vehicle_by_id(db: Session, vehicle_id: int):
    return db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()


def find_vehicle_by_number_plate(db: Session, number_plate: str):
    return db.query(Vehicle).filter(Vehicle.number_plate == number_plate).first()


def find_vehicle_by_manufacturer(db: Session, manufacturer: str):
    return db.query(Vehicle).filter(Vehicle.manufacturer == manufacturer).all()


def find_vehicles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Vehicle).offset(skip).limit(limit).all()


def create_vehicle(db: Session, vehicle: VehicleCreate):
    db_vehicle = Vehicle(manufacturer=vehicle.manufacturer, model=vehicle.model, year=vehicle.year,
                         number_plate=vehicle.number_plate)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)

    assignment = OwnerVehicleAssignmentCreate(vehicle_id=db_vehicle.id, owner_id=vehicle.owner_id,
                                              centre_id=vehicle.centre_id)
    assign_owner_to_vehicle(db, assignment)
    return db_vehicle


def assign_owner_to_vehicle(db: Session, assignment: OwnerVehicleAssignmentCreate):
    db_assignment = OwnerVehicleAssignment(vehicle_id=assignment.vehicle_id, owner_id=assignment.owner_id,
                                           centre_id=assignment.centre_id)
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment
