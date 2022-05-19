from typing import List, Dict, Optional, Union

from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate
from app.core.security import verify_password

from app.core.security import get_password_hash


class CRUDCompany(CRUDBase[Company, CompanyCreate, CompanyUpdate]):

    def create(self, db: Session, *, obj_in: CompanyCreate) -> Company:
        db_obj = Company(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            name=obj_in.name,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_email(self, db: Session, *, email: str) -> Optional[Company]:
        return db.query(Company).filter(Company.email == email).first()

    def authenticate(self, db: Session, *, email: str,
                     password: str) -> Optional[Company]:
        company = self.get_by_email(db, email=email)
        if not company:
            return None
        if not verify_password(password, company.hashed_password):
            return None
        return company

company = CRUDCompany(Company)