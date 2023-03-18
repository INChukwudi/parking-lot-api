from models.owner import Owner
from sqlalchemy.orm import Session

from schemas.owner import OwnerCreate
from utils.pwd_context import get_password_hash


def find_owner_by_id(db: Session, owner_id: int):
    return db.query(Owner).filter(Owner.id == owner_id).first()


def find_owner_by_email(db: Session, email: str):
    return db.query(Owner).filter(Owner.email == email).first()


def find_owners(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Owner).offset(skip).limit(limit).all()


def create_owner(db: Session, owner: OwnerCreate):
    password_hash = get_password_hash(owner.password)
    db_owner = Owner(firstName=owner.firstName, lastName=owner.lastName, email=owner.email, dob=owner.dob,
                     gender=owner.gender, passport=owner.passport, password=password_hash)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner
