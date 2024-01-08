# ------------------------------ Lib -------------------------------------- #
from passlib.context import CryptContext
from enum import Enum as PyEnum

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashed_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)