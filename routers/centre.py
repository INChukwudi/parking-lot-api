from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database.config import get_db
from repositories import centre
from schemas.centre import Centre, CentreCreate
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/centre",
    tags=["Centres"],
    dependencies=[Depends(get_current_user)]
)


@router.get("/", response_model=List[Centre])
def get_all(db: Session = Depends(get_db), skip=0, limit=100):
    return centre.find_centres(db, skip, limit)


@router.get("/{centre_id}", response_model=Centre)
def get_centre(centre_id: int, db: Session = Depends(get_db)):
    db_centre = centre.find_centre_by_id(db, centre_id)
    if db_centre is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Centre not found")
    return db_centre


@router.post("/", response_model=Centre)
def create_centre(centre_create: CentreCreate, db: Session = Depends(get_db)):
    # Name Check
    db_centre = centre.find_centre_by_name(db, name=centre_create.name)
    if db_centre:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Centre name already exists")

    # Address Check
    db_centre = centre.find_centre_by_address(db, address=centre_create.address)
    if db_centre:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Centre address already exists")
    return centre.create_centre(db, centre_create)

