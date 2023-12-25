# config.py (at the root level)

from pydantic import BaseSettings

class GlobalConfig(BaseSettings):
    PROJECT_NAME: str = "fastapi_tools"
    DEBUG: bool = False

# Create an instance of the GlobalConfig
global_config = GlobalConfig()
