from typing import Optional, List
from datetime import datetime, date
from pydantic import BaseModel



class EmployeeBase(BaseModel):
    full_name: str
    doc_number: str
    phone: str
    email: str
    password: str
    mine_id: int

class EmployeeCreate(EmployeeBase):
    ...

class EmployeeUpdate(EmployeeBase):
    ...

class EmployeeInDBBase(BaseModel):
    id: int
    full_name: str
    doc_number: str
    phone: str
    email: str
    mine_id: int

    class Config:
        orm_mode = True


class Employee(EmployeeInDBBase):
    ...


class EmployeeInDB(EmployeeInDBBase):
    hashed_password: str
