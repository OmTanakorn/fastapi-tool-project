
from fastapi import APIRouter, Depends, Form, HTTPException, status
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
    permission: service.Permission = service.Permission.Viewer,  # กำหนดค่าเริ่มต้นเป็น Viewer หรือค่าที่ต้องการ
    db: SessionLocal = Depends(get_db)
):
    user = service.create_user(db, form_data.username, form_data.password, permission)

    return {"message": "User registered successfully"}
