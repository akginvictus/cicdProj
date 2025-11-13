"""
Backward-compatible exports for configuration values.
"""

from .app.config import Config

_config = Config()

POSTGRES_HOST = _config.POSTGRES_HOST
POSTGRES_DB = _config.POSTGRES_DB
POSTGRES_USER = _config.POSTGRES_USER
POSTGRES_PASSWORD = _config.POSTGRES_PASSWORD

REDIS_HOST = _config.REDIS_HOST
REDIS_PORT = _config.REDIS_PORT

__all__ = [
    "Config",
    "POSTGRES_HOST",
    "POSTGRES_DB",
    "POSTGRES_USER",
    "POSTGRES_PASSWORD",
    "REDIS_HOST",
    "REDIS_PORT",
]
