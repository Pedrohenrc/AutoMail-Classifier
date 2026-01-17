from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    GEMINI_API_KEY: str = Field(..., description="Gemini API Key")
    GEMINI_MODEL: str = "gemini‑2.5‑flash‑lite"
    PORT: int = 8000

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
    }


settings = Settings()
