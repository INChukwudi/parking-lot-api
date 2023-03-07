from models.admin import Admin
from sqlalchemy.orm import Session

from schemas.admin import AdminCreate


def find_admin_by_id(db: Session, admin_id: int):
    return db.query(Admin).filter(Admin.id == admin_id).first()


def find_admin_by_email(db: Session, email: str):
    return db.query(Admin).filter(Admin.email == email).first()


def find_admins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Admin).offset(skip).limit(limit).all()


def create_admin(db: Session, admin: AdminCreate):
    db_admin = Admin(firstName=admin.firstName, lastName=admin.lastName, email=admin.email, password=admin.password,
                     level=admin.level, centre_id=admin.centre_id)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin
