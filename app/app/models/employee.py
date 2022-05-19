from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base, DateTimeMixin


class Employee(Base, DateTimeMixin):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    doc_number = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    mine_id = Column(Integer, ForeignKey('mine.id'), nullable=False)
    company_id = Column(Integer, ForeignKey('company.id'), nullable=False)

    mine = relationship('Mine', backref='employers')
    company = relationship('Company', backref='employers')