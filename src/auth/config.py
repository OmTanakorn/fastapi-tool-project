from pydantic import BaseSettings

class AuthConfig(BaseSettings):
  SECRET_KEY: str
  ALGORITHM: str = "HS256"
  ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

auth_config = AuthConfig()