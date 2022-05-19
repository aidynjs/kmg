from datetime import timedelta
from starlette.exceptions import HTTPException
from typing import List, Any
from fastapi import APIRouter, Depends
from app import schemas, crud, models
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core import security

from . import deps

router = APIRouter()


@router.post("/", response_model=schemas.Employee)
def create_employee(
    *,
    db: Session = Depends(deps.get_db),
    employee_in: schemas.EmployeeCreate,
    current_company: models.Company = Depends(deps.get_current_company)
) -> Any:
    # validate mine
    mine = crud.mine.get(db, id=employee_in.mine_id)
    if not mine:
        raise HTTPException(status_code=404, detail='err')
    if mine.company_id != current_company.id:
        raise HTTPException(status_code=403, detail='err')

    employee = crud.employee.create(
        db=db,
        obj_in=employee_in,
        company_id=current_company.id
    )
    return employee


@router.post("/login")
def employee_login(
    *,
    db: Session = Depends(deps.get_db),
    auth_in: schemas.Auth
) -> Any:
    employee = crud.employee.authenticate(
        db, email=auth_in.email, password=auth_in.password
    )
    if not employee:
        raise HTTPException(status_code=400, detail="err")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token_user(
            employee.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer"
    }