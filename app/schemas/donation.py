# app/schemas/donation.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt


class DonationCreate(BaseModel):
    """Schema for Donation Create."""

    comment: Optional[str]
    full_amount: PositiveInt


class DonationPartDB(DonationCreate):
    """Schema for Donation Create."""

    id: int
    create_date: datetime
    user_id: Optional[int]

    class Config:
        orm_mode = True


class DonationFullDB(DonationPartDB):
    """Schema to display all Donation object data"""

    invested_amount: Optional[int]
    fully_invested: Optional[bool]
    close_date: Optional[datetime]
