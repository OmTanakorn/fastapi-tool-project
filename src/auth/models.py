from sqlalchemy import Column, String, Integer
from src.database import Base

class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    password = Column(String)
