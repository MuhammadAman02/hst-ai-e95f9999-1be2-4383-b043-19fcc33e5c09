from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    APP_NAME: str = "My Enterprise App"
    APP_VERSION: str = "1.0.0"  # Semantic versioning
    APP_ENV: str = os.getenv("APP_ENV", "development")
    DEBUG: bool = False
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./default.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "a_very_secret_key")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_file = ".env"

settings = Settings()