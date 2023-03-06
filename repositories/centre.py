from models.centre import Centre
from sqlalchemy.orm import Session


def find_centre_by_id(db: Session, centre_id: int):
    return db.query(Centre).filter(Centre.id == centre_id).first()


def find_centre_by_name(db: Session, name: str):
    return db.query(Centre).filter(Centre.name == name).first()


def find_centre_by_address(db: Session, address: str):
    return db.query(Centre).filter(Centre.address == address).first()


def find_centres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Centre).offset(skip).limit(limit).all()
