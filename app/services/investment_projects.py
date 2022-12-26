# app/services/investment_projects.py
from datetime import datetime
from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charity_project_crud, donation_crud
from app.models import CharityProject, Donation


def closing(db_obj: Union[Donation, CharityProject]) -> None:
    db_obj.fully_invested = True
    db_obj.invested_amount = db_obj.full_amount
    db_obj.close_date = datetime.now()


async def investment_when_create(session: AsyncSession) -> None:
    all_charity_projects = await charity_project_crud.get_not_closed(session)
    all_donations = await donation_crud.get_not_closed(session)
    # Если один из списков пустой - пропускаем распределение пожертвований
    if not all([all_charity_projects, all_donations]):
        return
    for charity_project in all_charity_projects:
        for donation in all_donations:
            need_money = (
                charity_project.full_amount - charity_project.invested_amount
            )
            available_money = donation.full_amount - donation.invested_amount
            money_left = need_money - available_money

            if money_left == 0:
                closing(charity_project)
                closing(donation)

            if money_left < 0:
                # abs - возвращает абсолютное число (без минуса)
                donation.invested_amount += abs(money_left)
                closing(charity_project)

            if money_left > 0:
                charity_project.invested_amount += available_money
                closing(donation)
