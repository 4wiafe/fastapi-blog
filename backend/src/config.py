from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, Field

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
    )

    database_url: PostgresDsn = Field(repr=False)


settings = Settings()  # type: ignore
