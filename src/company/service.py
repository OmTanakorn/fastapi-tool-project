# ------------------------------ Lib -------------------------------------- #

# ------------------------------ from app --------------------------------- #
from src.database import SessionLocal
from src.company import models, schemas
from src.auth.service import create_user


def create_company(db: SessionLocal, company_create: schemas.CompanyCreate):
    company = models.Company(**company_create.dict())
    db.add(company)
    db.commit()
    db.refresh(company)
    return company

def get_company(db: SessionLocal, company_id: int):
    Company = models.Company
    return db.query(Company).filter(Company.id == company_id).first()
    
