import os

class Settings:
    """
    Configuration settings for the app.
    """
    APP_NAME: str = os.getenv("APP_NAME", "TaskManager")
    APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")

settings = Settings()