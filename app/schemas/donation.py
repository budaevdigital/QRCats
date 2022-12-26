# app/schemas/donation.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt


class DonationCreate(BaseModel):
    """Схема создания пожертвования."""

    comment: Optional[str]
    full_amount: PositiveInt


class DonationPartDB(DonationCreate):
    """Схема создания пожертвования."""

    id: int
    create_date: datetime
    user_id: Optional[int]

    class Config:
        orm_mode = True


class DonationFullDB(DonationPartDB):
    """Схема для отображения всех данных объекта пожертвования"""

    invested_amount: Optional[int]
    fully_invested: Optional[bool]
    close_date: Optional[datetime]
