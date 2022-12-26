# app/api/endpoints/charity_project.py
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_charity_invested_before_delete,
    check_charity_is_closed,
    check_charity_new_and_old_amount,
    check_name_duplicate,
    check_project_exists,
)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.schemas.charity_project import (
    CharityProjectCreate,
    CharityProjectDB,
    CharityProjectUpdate,
)
from app.services.investment_projects import investment_when_create

router = APIRouter()


@router.get(
    "/",
    response_model=List[CharityProjectDB],
    response_model_exclude_none=True,
    summary="Получить весь список проектов",
)
async def get_all_charity_projects(
    session: AsyncSession = Depends(get_async_session),
):
    """Запрос на получение всех проектов"""
    return await charity_project_crud.get_multi(session)


@router.post(
    "/",
    dependencies=[Depends(current_superuser)],
    summary="Создание благотворительного проекта",
    response_model=CharityProjectDB,
)
async def create_charity_project(
    charity_obj: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """
    (Только для суперпользователей)

    Создаёт благотворительный проект
    """
    await check_name_duplicate(charity_obj.name, session)
    new_charity_obj = await charity_project_crud.create(charity_obj, session)
    await investment_when_create(session)
    await session.commit()
    await session.refresh(new_charity_obj)
    return new_charity_obj


@router.delete(
    "/{project_id}",
    summary="Удаление благотворительного проекта",
    dependencies=[Depends(current_superuser)],
    response_model=CharityProjectDB,
)
async def remove_charity_project(
    project_id: int, session: AsyncSession = Depends(get_async_session)
):
    """
    (Только для супер пользователей)

    Удаляет благотворительный проект

    Нельзя удалить проект, в который уже была внесена сумма пожертвований -
     его можно только изменить
    """
    charity_obj = await check_project_exists(
        charity_id=project_id, session=session
    )
    await check_charity_is_closed(charity_obj)
    await check_charity_invested_before_delete(charity_obj)
    return await charity_project_crud.remove(charity_obj, session)


@router.patch(
    "/{project_id}",
    dependencies=[Depends(current_superuser)],
    summary="Изменяет благотворительный проект",
    response_model=CharityProjectDB,
)
async def update_charity_project(
    project_id: int,
    new_charity_obj: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """
    (Только для супер пользователей)

    Изменяет благотворительный проект

    Новая сумма проекта должна быть не ниже уже пожертвованной суммы
    """
    charity_obj = await check_project_exists(
        charity_id=project_id, session=session
    )
    if new_charity_obj.name:
        await check_name_duplicate(new_charity_obj.name, session)
    if new_charity_obj.full_amount:
        await check_charity_new_and_old_amount(
            charity_obj, new_charity_obj.full_amount
        )
    new_charity_obj = await charity_project_crud.update(
        charity_obj, new_charity_obj, session
    )
    return new_charity_obj
