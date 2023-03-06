from models.owner import Owner
from sqlalchemy.orm import Session


def find_owner_by_id(db: Session, owner_id: int):
    return db.query(Owner).filter(Owner.id == owner_id).first()


def find_owner_by_email(db: Session, email: str):
    return db.query(Owner).filter(Owner.email == email).first()


def find_owners(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Owner).offset(skip).limit(limit).all()
