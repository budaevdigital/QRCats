# app/schemas/charity_project.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt, validator


class CharityProjectBase(BaseModel):
    """Schema for Project Base."""

    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectBase):
    """Schema for Project Create."""

    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt

    @validator("name", "description")
    def check_for_empty_and_none(cls, value: str):
        if not value or value is None:
            raise ValueError("Fields must not be empty")
        return value


class CharityProjectUpdate(CharityProjectBase):
    """Schema for Project Update."""

    pass


class CharityProjectDB(CharityProjectBase):
    """Schema for Project in DB."""

    id: int
    invested_amount: Optional[int]
    fully_invested: Optional[int]
    create_date: Optional[datetime]
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
