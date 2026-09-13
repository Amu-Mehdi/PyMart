from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings — read from the .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    APP_NAME: str = "PyMart"
    ENV: str = "development"
    SECRET_KEY: str = "change-me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DATABASE_URL: str = "sqlite:///./pymart.db"
    REDIS_URL: str = "redis://localhost:6379/0"
    UPLOAD_DIR: str = "app/static/uploads"


@lru_cache
def get_settings() -> Settings:
    """It returns a singleton instance of Settings (it gets cached)."""
    return Settings()