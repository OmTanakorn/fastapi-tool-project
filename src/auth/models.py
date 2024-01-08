# ------------------------------ Lib -------------------------------------- #
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


# ------------------------------ from app --------------------------------- #
from src.models import BaseModel
from src.auth.schemas import Permission
from src.company.models import Company

class User(BaseModel):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    permission = Column(Integer)
    company_id = Column(Integer, ForeignKey('companies.id'))

    company = relationship("Company", back_populates="users")
