from typing import Optional, List
from datetime import datetime, date
from pydantic import BaseModel



# Shared properties
class CompanyBase(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    

class CompanyCreate(CompanyBase):
    email: str
    password: str


class CompanyUpdate(CompanyBase):
    password: Optional[str] = None


class CompanyInDBBase(CompanyBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Company(CompanyInDBBase):
    ...


class CompanyInDB(CompanyInDBBase):
    hashed_password: str
