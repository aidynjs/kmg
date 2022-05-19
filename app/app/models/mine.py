from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base, DateTimeMixin


class Mine(Base, DateTimeMixin):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey('company.id'))
    company = relationship('Company', backref='mines')