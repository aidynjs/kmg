from datetime import timedelta
from starlette.exceptions import HTTPException
from typing import List, Any
from fastapi import APIRouter, Depends
from app import schemas, crud
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core import security
from . import deps

router = APIRouter()


@router.post("/login")
def company_login(
    *,
    db: Session = Depends(deps.get_db),
    auth_in: schemas.Auth
) -> Any:
    company = crud.company.authenticate(
        db, email=auth_in.email, password=auth_in.password
    )
    if not company:
        raise HTTPException(status_code=400, detail="err")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token_company(
            company.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer"
    }

@router.post("/", response_model=schemas.Company)
def create_company(
    *,
    db: Session = Depends(deps.get_db),
    company_in: schemas.CompanyCreate,
) -> Any:
    comapny = crud.company.get_by_email(db, email=company_in.email)
    if comapny:
        raise HTTPException(
            status_code=400,
            detail="err"
        )
    company = crud.company.create(db, obj_in=company_in)
    return company




    