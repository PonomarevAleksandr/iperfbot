"""ENV SETTINGS"""
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings class
    """
    BOT_TOKEN: str


    model_config = SettingsConfigDict(env_file="/app/.env")


settings = Settings()
