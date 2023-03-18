from datetime import timedelta

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from database.config import Base, engine, get_db
from routers import admin, centre, vehicle, owner
from repositories import admin as admin_repo
from schemas.admin import Admin, AdminCreate
from schemas.token import Token
from utils.jwt_access import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from utils.pwd_context import verify_password

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World! Welcome to the Secure Park API."}


@app.post("/login", response_model=Token, tags=["Auth"])
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = admin_repo.find_admin_by_email(db, email=form_data.username)
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


@app.post("/", response_model=Admin, status_code=status.HTTP_201_CREATED)
def create_admin(admin_create: AdminCreate, db: Session = Depends(get_db)):
    db_admin = admin_repo.find_admin_by_email(db, email=admin_create.email)
    if db_admin:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email is in use")
    return admin_repo.create_admin(db, admin_create)


app.include_router(admin.router)
app.include_router(centre.router)
app.include_router(owner.router)
app.include_router(vehicle.router)
