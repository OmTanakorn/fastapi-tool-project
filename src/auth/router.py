# src/auth/router.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.auth import dependencies, models, schemas, service
from src.auth.config import auth_config
from src.database import SessionLocal, get_db

router = APIRouter()

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: SessionLocal = Depends(get_db)):
    user = service.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {"access_token": service.create_access_token(data={"sub": user.username})}

@router.post("/register")
def register_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: SessionLocal = Depends(get_db)
):
    # Validate form_data, check if user already exists, etc.
    # You can implement the user registration logic here using your service functions

    # For example, assuming you have a function like create_user
    user = service.create_user(db, form_data.username, form_data.password)

    return {"message": "User registered successfully"}


@router.get("/users/me", response_model=models.User)
async def read_users_me(current_user: models.User = Depends(dependencies.get_current_user)):
    return current_user
