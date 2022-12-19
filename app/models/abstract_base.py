# app/models/abstract_base.py
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Boolean
from app.core.db import Base


class AbstractBaseModel(Base):

    __abstract__ = True

    full_amount = Column(Integer, default=0)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    # To record different date and time values, we pass not a function call,
    # but the function itself (datetime.now)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime, default=None, nullable=True)
