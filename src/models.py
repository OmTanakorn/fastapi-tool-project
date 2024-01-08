# ------------------------------ Lib -------------------------------------- #
from datetime import datetime
from sqlalchemy import Column, DateTime, String

# ------------------------------ from app --------------------------------- #
from src.database import Base

class BaseModel(Base):
    __abstract__ = True

    is_delete = Column(DateTime, nullable=True, default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

