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


@router.post("/", response_model=schemas.Mine)
def create_mine(
    *,
    db: Session = Depends(deps.get_db),
    mine_in: schemas.MineCreate,
    current_company: models.Company = Depends(deps.get_current_company)
) -> Any:
    mine = crud.mine.create(
        db=db,
        obj_in=mine_in,
        company_id=current_company.id
    )
    return mine