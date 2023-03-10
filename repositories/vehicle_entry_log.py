from models.vehicle_entry_log import VehicleEntryLog
from sqlalchemy.orm import Session

from schemas.vehicle_entry_log import VehicleEntryLogCreate


def find_vehicle_entry_log_by_log_id(db: Session, log_id: int):
    return db.query(VehicleEntryLog).filter(VehicleEntryLog.id == log_id).first()


def find_vehicle_entry_log_by_vehicle_id(db: Session, vehicle_id: int):
    return db.query(VehicleEntryLog).filter(VehicleEntryLog.vehicle_id == vehicle_id).all()


def find_vehicle_entry_log_by_owner_id(db: Session, owner_id: int):
    return db.query(VehicleEntryLog).filter(VehicleEntryLog.owner_id == owner_id).all()


def find_vehicle_entry_log_by_centre_id(db: Session, centre_id: int):
    return db.query(VehicleEntryLog).filter(VehicleEntryLog.centre_id == centre_id).all()


def find_vehicle_entry_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(VehicleEntryLog).offset(skip).limit(limit).all()


def create_vehicle_entry_log(db: Session, entry_log: VehicleEntryLogCreate):
    db_log = VehicleEntryLog(**entry_log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log
