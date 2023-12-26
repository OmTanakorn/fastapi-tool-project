# models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from src.database import Base
# Base = declarative_base()




# Example SQLAlchemy model
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
