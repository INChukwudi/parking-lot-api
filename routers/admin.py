from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database.config import get_db
from repositories import admin
from schemas.admin import Admin, AdminCreate
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/admin",
    tags=["Admins"],
    dependencies=[Depends(get_current_user)]
)


@router.get("/", response_model=List[Admin])
def get_all(db: Session = Depends(get_db), skip=0, limit=100, current_admin: Admin = Depends(get_current_user)):
    return admin.find_admins(db, skip, limit)


@router.get("/{admin_id}", response_model=Admin)
def get_admin(admin_id: int, db: Session = Depends(get_db)):
    db_admin = admin.find_admin_by_id(db, admin_id)
    if db_admin is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Admin not found")
    return db_admin


@router.post("/", response_model=Admin, status_code=status.HTTP_201_CREATED)
def create_admin(admin_create: AdminCreate, db: Session = Depends(get_db)):
    db_admin = admin.find_admin_by_email(db, email=admin_create.email)
    if db_admin:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email is in use")
    return admin.create_admin(db, admin_create)

