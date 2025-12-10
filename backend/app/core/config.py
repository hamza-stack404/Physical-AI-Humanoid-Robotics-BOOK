from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://user:password@host:port/database"
    QDRANT_URL: str = "http://localhost:6333" # Placeholder

    class Config:
        env_file = ".env"

settings = Settings()
