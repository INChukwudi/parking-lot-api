from models.admin import Admin
from sqlalchemy.orm import Session


def find_admin_by_id(db: Session, admin_id: int):
    return db.query(Admin).filter(Admin.id == admin_id).first()


def find_admin_by_email(db: Session, email: str):
    return db.query(Admin).filter(Admin.email == email).first()


def find_admins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Admin).offset(skip).limit(limit).all()
