# app/schemas/donation.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt


class DonationBase(BaseModel):
    """Schema for Donation Base."""

    comment: Optional[str]
    fully_amount: PositiveInt


class DonationCreate(DonationBase):
    """Schema for Donation Create."""

    id: int
    user_id: Optional[int]
    create_date: datetime

    class Config:
        orm_mode = True


class DonationFull(DonationCreate):
    """Schema to display all Donation object data"""

    invested_amount: Optional[int]
    fully_invested: Optional[bool]
    close_date: Optional[datetime]
