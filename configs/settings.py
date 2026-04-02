from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # App identity
    app_name: str = "enterprise-ai-platform"
    app_env: str = "development"
    debug: bool = True

    # OpenAI
    openai_api_key: str = ""

    # Database
    database_url: str = "sqlite:///./app.db"

    # Redis
    redis_url: str = "redis://localhost:6379"

    # JWT Auth
    jwt_secret_key: str = "change-me"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 30

    # MLflow
    mlflow_tracking_uri: str = "http://localhost:5000"

    # Vector Store
    vector_store_path: str = "./data/vector_store"

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    return Settings()