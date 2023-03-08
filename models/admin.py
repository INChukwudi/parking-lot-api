from database.config import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False, index=True, unique=True)
    password = Column(String, nullable=False)
    level = Column(Integer, default=1)
    centre_id = Column(Integer, ForeignKey("centres.id"), nullable=True)

    centre = relationship("Centre", back_populates="admins")
