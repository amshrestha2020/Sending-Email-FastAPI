import os
from dotenv import load_dotenv

from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    EMAIL_FROM = os.getenv("EMAIL_FROM","admin@admin.com")
    BREVO_API_KEY: str = os.getenv("BREVO_API_KEY")


settings = Settings()