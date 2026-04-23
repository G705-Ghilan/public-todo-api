from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mongodb_url: str

    # model_config = SettingsConfigDict(env_file='.env')
    model_config = SettingsConfigDict(env_file='env.development')


# Cached settings loader (reads from .env only once)
@lru_cache
def get_settings():
    return Settings()


# Settings dependency for FastAPI endpoints
SettingsDep = Annotated[Settings, Depends(get_settings)]
