# """
# Compatibility re-export layer for the old import path.

# Azure and tests expect Config to be importable at:
#     from FlaskWebProject1.config import Config
# """

# from FlaskWebProject1.app.config import Config

# _config = Config()

# POSTGRES_HOST = _config.POSTGRES_HOST
# POSTGRES_DB = _config.POSTGRES_DB
# POSTGRES_USER = _config.POSTGRES_USER
# POSTGRES_PASSWORD = _config.POSTGRES_PASSWORD

# REDIS_HOST = _config.REDIS_HOST
# REDIS_PORT = _config.REDIS_PORT

# __all__ = [
#     "Config",
#     "POSTGRES_HOST",
#     "POSTGRES_DB",
#     "POSTGRES_USER",
#     "POSTGRES_PASSWORD",
#     "REDIS_HOST",
#     "REDIS_PORT",
# ]
import os
from dataclasses import dataclass

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
