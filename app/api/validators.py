# app/api/validators.py
from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charity_project_crud
from app.models import CharityProject


async def check_name_duplicate(
    charity_name: str, session: AsyncSession
) -> None:
    charity_id = await charity_project_crud.get_id_by_name(
        charity_name=charity_name, session=session
    )
    if charity_id is not None:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail="Проект с таким именем уже существует!",
        )


async def check_project_exists(
    charity_id: int, session: AsyncSession
) -> CharityProject:
    charity_obj = await charity_project_crud.get(
        obj_id=charity_id, session=session
    )
    if charity_obj is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Такой проект не найден"
        )
    return charity_obj


async def check_charity_is_closed(
    charity_obj: CharityProject,
) -> None:
    if charity_obj.fully_invested:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail="Закрытые проекты нельзя удалять или редактировать!",
        )


async def check_charity_new_and_old_amount(
    charity_obj: CharityProject, new_amount: int
) -> None:
    if new_amount is not None:
        if new_amount <= charity_obj.invested_amount:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail=(
                    "Новая запрашиваемая сумма не может быть ниже "
                    "уже внесённых пожертвований!"
                ),
            )


async def check_charity_invested_before_delete(
    charity_obj: CharityProject,
) -> None:
    if charity_obj.invested_amount > 0:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail=(
                "Проект не может быть удалён "
                "из-за наличия в нём пожертвований"
            ),
        )
