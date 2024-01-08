# ------------------------------ Lib -------------------------------------- #
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.auth import service
from src.auth.config import auth_config
from src.database import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



def get_db_session() -> Session:
    db = get_db()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return service.get_current_user(token, credentials_exception, auth_config)
