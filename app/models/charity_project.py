# app/models/charityproject.py
from sqlalchemy import Column, String, Text

from app.models.abstract_base import AbstractBaseModel


class CharityProject(AbstractBaseModel):
    """Модель представления благотворительного фонда в базе данных"""

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return (
            f"CharityProject(name={self.name}, full_amount={self.full_amount})"
        )

    def __str__(self) -> str:
        return f"Проект: {self.name}, Нужно денег: {self.full_amount}"
