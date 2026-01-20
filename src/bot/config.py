from functools import lru_cache
from pathlib import Path
from pydantic import BaseSettings, Field, SettingsConfigDict


class Settings(BaseSettings):
    llm_provider: str = Field("ollama", description="ollama|openai")
    ollama_base_url: str = "http://localhost:11434"
    openai_api_key: str | None = None

    google_calendar_id: str = ""
    google_drive_history_file_id: str = ""
    google_token_path: Path = Path(".tokens/google.json")
    google_credentials_path: Path = Path("credentials.json")
    greeting_history_local_cache: Path = Path(".cache/greetings_history.json")
    birthday_label: str = "birthday"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


def resolve_path(path: Path) -> Path:
    return path.expanduser().resolve()


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    settings = Settings()
    settings.google_token_path = resolve_path(settings.google_token_path)
    settings.google_credentials_path = resolve_path(settings.google_credentials_path)
    settings.greeting_history_local_cache = resolve_path(settings.greeting_history_local_cache)
    return settings
