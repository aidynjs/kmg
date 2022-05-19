from typing import Generator
from app.db.session import SessionLocal
from app.schemas import company
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException
from jose import jwt
from fastapi import Depends
from app.core import security
from app.core.config import settings
from app import models, crud

bearer_token = HTTPBearer()

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_company(
    db: Session = Depends(get_db), token: str = Depends(bearer_token)
) -> models.Company:
    try:
        payload = jwt.decode(
            token.credentials, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
    except (jwt.JWTError) as e:
        raise HTTPException(
            status_code=403,
            detail=e,
        )
    if payload['type'] != 1:
        raise HTTPException(status_code=403, detail=payload)
    company = crud.company.get(db, id=payload['sub'])
    if not company:
        raise HTTPException(status_code=404, detail="err")
    return company