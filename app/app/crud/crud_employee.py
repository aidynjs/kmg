from app.models import employee
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

from app.core.security import verify_password
from app.core.security import get_password_hash


class CRUDEmployee(CRUDBase[Employee, EmployeeCreate, EmployeeUpdate]):

    def get_by_email(self, db: Session, *, email: str):
        return db.query(Employee).filter(Employee.email == email).first()

    def create(self, db: Session, *, obj_in: EmployeeCreate,
               company_id: int) -> Employee:
        employee = self.model(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            doc_number=obj_in.doc_number,
            phone=obj_in.phone,
            mine_id=obj_in.mine_id,
            company_id=company_id
        )
        db.add(employee)
        db.commit()
        db.refresh(employee)
        return employee

    def authenticate(self, db: Session, *, email: str,
                     password: str):
        employee = self.get_by_email(db, email=email)
        if not employee:
            return None
        if not verify_password(password, employee.hashed_password):
            return None
        return employee

employee = CRUDEmployee(Employee)