# config.py (at the root level)
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class GlobalConfig(BaseSettings):
    
    PROJECT_NAME: str = "fastapi_tools"
    DEBUG: bool = False
    

class DatabaseConfig(BaseSettings):
    DATABASE_URL: str

# Create an instance of the GlobalConfig
global_config = GlobalConfig()
database_config = DatabaseConfig()
