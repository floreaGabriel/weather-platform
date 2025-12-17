import os


class Settings:
    """Application settings loaded from environment variables."""

    APP_NAME: str = os.getenv("APP_NAME", "weather-prediction-api")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    VERSION: str = os.getenv("VERSION", "0.1.0")


settings = Settings()
