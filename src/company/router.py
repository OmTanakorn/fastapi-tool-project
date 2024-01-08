# ------------------------------ Lib -------------------------------------- #
from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

# ------------------------------ from app --------------------------------- #
from src.company import schemas, service
from src.database import SessionLocal, get_db

router = APIRouter()

@router.post("/company/")
def create_company(company_create: schemas.CompanyCreate, db: SessionLocal = Depends(get_db)):
    company = service.create_company(db, company_create)
    return {"message": "Create Company successfully"}

@router.get("/companies/{company_id}", response_model=schemas.Company)
def read_company(company_id: int, db: SessionLocal = Depends(get_db)):
    company = service.get_company(db=db, company_id=company_id)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company
