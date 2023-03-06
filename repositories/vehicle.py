from models.vehicle import Vehicle
from sqlalchemy.orm import Session


def find_vehicle_by_id(db: Session, vehicle_id: int):
    return db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()


def find_vehicle_by_number_plate(db: Session, number_plate: str):
    return db.query(Vehicle).filter(Vehicle.number_plate == number_plate).first()


def find_vehicle_by_manufacturer(db: Session, manufacturer: str):
    return db.query(Vehicle).filter(Vehicle.manufacturer == manufacturer).first()


def find_vehicles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Vehicle).offset(skip).limit(limit).all()
