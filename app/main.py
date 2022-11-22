# app/main.py
from fastapi import FastAPI
import uvicorn

# Импортируем настройки проекта
from core.config import settings

app = FastAPI(title=settings.app_title)

if __name__ == "__main__":
    uvicorn.run("__main__:app", reload=True, env_file=".env")
