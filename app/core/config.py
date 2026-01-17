import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = "gemini-2.5-flash"
    PORT: int = 8000

    class Config:
        env_file = ".env"
        case_sensitive = True
        
    @classmethod
    def validate(cls):
        if not cls.GEMINI_API_KEY:
            raise RuntimeError("GEMINI_API_KEY not configured")


settings = Settings()
settings.validate()
