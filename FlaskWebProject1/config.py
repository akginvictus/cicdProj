import os
from dataclasses import dataclass

@dataclass
class Config:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-key")

    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "db")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "appdb")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "appuser")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "1234")

    REDIS_HOST: str = os.getenv("REDIS_HOST", "redis")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))
