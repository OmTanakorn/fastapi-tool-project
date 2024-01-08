# ------------------------------ Lib -------------------------------------- #
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

# ------------------------------ from app --------------------------------- #
from src.models import BaseModel

class Company(BaseModel):
  __tablename__ = "companies"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)
  service = Column(Integer)

  users = relationship("User", back_populates="company")