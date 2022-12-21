# app/crud/charity_project.py
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):
    async def get_name_by_id(
        self, charity_name: str, session: AsyncSession
    ) -> Optional[int]:
        db_charity_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charity_name
            )
        )
        db_charity_id = db_charity_id.scalars().first()
        return db_charity_id

    async def get_project_by_id(
        self, charity_id: int, session: AsyncSession
    ) -> Optional[CharityProject]:
        db_charity = await session.execute(
            select(CharityProject).where(CharityProject.id == charity_id)
        )
        db_charity = db_charity.scalars().first()
        return db_charity


charity_project_crud = CRUDCharityProject(CharityProject)
