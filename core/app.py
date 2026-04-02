from fastapi import FastAPI
from configs.settings import get_settings
from core.logger import logger

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)


@app.get("/")
def health_check():
    logger.info("Health check endpoint called")

    return {
        "status": "ok",
        "app": settings.app_name,
        "env": settings.app_env,
    }