# app/core/config.py
from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    # Нужно явно описать необходимые переменные без учета регистра
    app_title: str = "QRCats - приложение для помощи котикам!"
    app_description: str = (
        "Фонд собирает пожертвования на различные "
        "целевые проекты: на медицинское обслуживание нуждающихся хвостатых, "
        "на обустройство кошачьей колонии в подвале, на корм оставшимся без "
        "попечения кошкам — на любые цели, связанные "
        "с поддержкой кошачьей популяции."
    )
    app_version: str = "0.1.0"
    database_url: str = "sqlite+aiosqlite:///./fastapi.db"
    secret_key: str = "SECRETaidwoksopQOIWJdskdsh"
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()
