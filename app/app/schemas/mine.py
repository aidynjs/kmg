from typing import Optional
from pydantic import BaseModel



# Shared properties
class MineBase(BaseModel):
    name: str
    

class MineCreate(MineBase):
    ...

class MineUpdate(MineBase):
    ...

class MineInDBBase(MineBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class Mine(MineInDBBase):
    ...


class MineInDB(MineInDBBase):
    ...
