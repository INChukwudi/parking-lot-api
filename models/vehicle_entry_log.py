from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime

from database.config import Base


class VehicleEntryLog(Base):
    __tablename__ = "vehicle_entry_log"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), index=True)
    owner_id = Column(Integer, ForeignKey("owners.id"), index=True)
    centre_id = Column(Integer, ForeignKey("centres.id"), index=True)
    entry_date_time = Column(DateTime, nullable=False, default=datetime.now())
    exit_date_time = Column(DateTime, nullable=True)
