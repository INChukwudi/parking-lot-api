from fastapi import FastAPI

from database.config import Base, engine
from routers import admin, centre, vehicle, owner

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(admin.router)
app.include_router(centre.router)
app.include_router(owner.router)
app.include_router(vehicle.router)


@app.get("/")
async def root():
    return {"message": "Hello World! Welcome to the Parking Lot API."}
