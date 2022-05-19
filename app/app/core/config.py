import os

from typing import Optional
from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    API_V1_STR = '/api/v1'
    SECRET_KEY: str = "test"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 2
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    class Config:
        case_sensitive = True

settings = Settings()
