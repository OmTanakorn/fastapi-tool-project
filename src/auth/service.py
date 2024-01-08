# ------------------------------ Lib -------------------------------------- #
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

# ------------------------------ from app --------------------------------- #
from src.database import SessionLocal
from src.auth import models
from src.auth.schemas import  Permission
from src.auth.config import auth_config
from src.auth.utils import verify_password, hashed_password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str, credentials_exception, auth_config):
    credentials = jwt.decode(token, auth_config.SECRET_KEY, algorithms=[auth_config.ALGORITHM])
    username: str = credentials.get("sub")
    if username is None:
        raise credentials_exception
    db = SessionLocal()
    user = db.query(models.User).filter(models.User.username == username).first()
    db.close()
    if user is None:
        raise credentials_exception
    return user


def authenticate_user(db, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or not verify_password(password, user.password):
        return None
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    expires = datetime.utcnow() + timedelta(minutes=auth_config.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, auth_config.SECRET_KEY, algorithm=auth_config.ALGORITHM)
    return encoded_jwt

def create_user(db: SessionLocal, username: str, password: str, permission: int):
    user = models.User(username=username, password=password, permission=permission)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


