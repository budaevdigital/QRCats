from pydantic import BaseSettings


class Settings(BaseSettings):
    # Нужно явно описать необходимые переменные без учета регистра
    app_title: str = "QRCats - приложение для помощи котикам"

    class Config:
        env_file = ".env"


settings = Settings()
