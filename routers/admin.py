from datetime import timedelta
from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database.config import get_db
from repositories import admin
from schemas.admin import Admin, AdminCreate
from utils.jwt_access import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from utils.pwd_context import verify_password

router = APIRouter(
    prefix="/admin",
    tags=["Admins"]
)


@router.get("/", response_model=List[Admin])
def get_all(db: Session = Depends(get_db), skip=0, limit=100):
    return admin.find_admins(db, skip, limit)


@router.get("/{admin_id}", response_model=Admin)
def get_admin(admin_id: int, db: Session = Depends(get_db)):
    db_admin = admin.find_admin_by_id(db, admin_id)
    if db_admin is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Admin not found")
    return db_admin


@router.post("/", response_model=Admin)
def create_admin(admin_create: AdminCreate, db: Session = Depends(get_db)):
    db_admin = admin.find_admin_by_email(db, email=admin_create.email)
    if db_admin:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email is in use")
    return admin.create_admin(db, admin_create)


def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = admin.find_admin_by_email(db, email=form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect email entered",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect password entered",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
