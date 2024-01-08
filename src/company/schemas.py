# ------------------------------ Lib -------------------------------------- #
from typing import List
from pydantic import BaseModel
from enum import IntEnum


from src.auth.schemas import User

class Service(IntEnum):
  Owner = 0
  ERC = 1
  Shipper = 2

class CompanyBase(BaseModel):
  name: str
  service: int

class CompanyCreate(CompanyBase):
  pass

class Company(CompanyBase):
  id: int
  users: List[User]
