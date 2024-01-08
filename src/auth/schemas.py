from pydantic import BaseModel
from enum import IntEnum

class Permission(IntEnum):
    Admin = 0
    Edit = 1
    Viewer = 2

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
    
class UserBase(BaseModel):
    permission : int

class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    username: str
