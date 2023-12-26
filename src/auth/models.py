from sqlalchemy import Column, String, Integer
from src.models import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    password = Column(String)
