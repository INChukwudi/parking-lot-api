from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database.config import get_db
from repositories import owner
from schemas.owner import Owner, OwnerCreate
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/owner",
    tags=["Owners"],
    dependencies=[Depends(get_current_user)]
)


@router.get("/", response_model=List[Owner])
def get_all(db: Session = Depends(get_db), skip=0, limit=100):
    return owner.find_owners(db, skip, limit)


@router.get("/{owner_id}", response_model=Owner)
def get_owner(owner_id: int, db: Session = Depends(get_db)):
    db_owner = owner.find_owner_by_id(db, owner_id)
    if db_owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found")
    return db_owner


@router.post("/", response_model=Owner)
def create_owner(owner_create: OwnerCreate, db: Session = Depends(get_db)):
    db_owner = owner.find_owner_by_email(db, email=owner_create.email.lower())
    if db_owner:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email is in use")
    return owner.create_owner(db, owner_create)

