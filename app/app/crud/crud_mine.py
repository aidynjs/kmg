from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.mine import Mine
from app.schemas.mine import MineCreate, MineUpdate



class CRUDMine(CRUDBase[Mine, MineCreate, MineUpdate]):

    def create(self, db: Session, *, obj_in: MineCreate,
               company_id: int) -> Mine:
        obj_in_data = jsonable_encoder(obj_in)
        mine = self.model(**obj_in_data, company_id=company_id)
        db.add(mine)
        db.commit()
        db.refresh(mine)
        return mine



mine = CRUDMine(Mine)