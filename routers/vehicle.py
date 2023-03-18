from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database.config import get_db
from repositories import vehicle
from schemas.vehicle import Vehicle, VehicleCreate
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/vehicle",
    tags=["Vehicles"],
    dependencies=[Depends(get_current_user)]
)


@router.get("/", response_model=List[Vehicle])
def get_all(db: Session = Depends(get_db), skip=0, limit=100):
    return vehicle.find_vehicles(db, skip, limit)


@router.get("/{vehicle_id}", response_model=Vehicle)
def get_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_vehicle = vehicle.find_vehicle_by_id(db, vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle not found")
    return db_vehicle


@router.post("/", response_model=Vehicle)
def create_vehicle(vehicle_create: VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = vehicle.find_vehicle_by_number_plate(db, number_plate=vehicle_create.number_plate)
    if db_vehicle:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Vehicle with number plate {vehicle_create.number_plate} already exists")
    return vehicle.create_vehicle(db, vehicle_create)

