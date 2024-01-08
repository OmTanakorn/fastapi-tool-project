# ------------------------------ Lib -------------------------------------- #
from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

# ------------------------------ from app --------------------------------- #
from src.config import global_config
from src.database import SessionLocal
from src.company.models import Company

from src.auth.router import router as auth_router
from src.company.router import router as company_router


# Create an instance of FastAPI
app = FastAPI(title=global_config.PROJECT_NAME, debug=global_config.DEBUG)

# def create_initial_data(db: Session):
#     # Check if initial data exists
#     company_count = db.query(Company).count()
#     if company_count == 0:
#         # Create initial data (e.g., Company A)
#         initial_company = Company(name="Company A", service=0)
#         db.add(initial_company)
#         db.commit()
#         db.refresh(initial_company)

# @app.on_event("startup")
# async def startup_event():
#     db = SessionLocal()
#     try:
#         create_initial_data(db)
#     finally:
#         db.close()


# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(company_router, prefix="/api/v1", tags=["API"])

