# ------------------------------ Lib -------------------------------------- #
from datetime import datetime
from sqlalchemy import Column, DateTime

# ------------------------------ from app --------------------------------- #
from src.database import Base

class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
