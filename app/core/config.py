import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = "gemini-2.5-flash"

    @classmethod
    def validate(cls):
        if not cls.OPENAI_API_KEY:
            raise RuntimeError("OPENAI_API_KEY not configured")


settings = Settings()
settings.validate()
