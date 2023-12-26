from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import database_config

# สร้าง engine สำหรับเชื่อมต่อกับฐานข้อมูล
engine = create_engine(database_config.DATABASE_URL)

# สร้าง SessionLocal สำหรับให้ใช้ใน Dependency
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# สร้าง Base สำหรับให้ SQLAlchemy ใช้เป็นตัวอ้างอิงในการประกาศโมเดล
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
