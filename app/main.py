# app/main.py
import uvicorn
from core.config import settings
from fastapi import FastAPI

app = FastAPI(title=settings.app_title, description=settings.app_description)

if __name__ == "__main__":
    uvicorn.run(
        "__main__:app", reload=True, env_file=".env", host="0.0.0.0", port=8000
    )
