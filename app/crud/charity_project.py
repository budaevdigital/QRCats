# app/crud/charity_project.py
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):
    async def get_id_by_name(
        self, charity_name: str, session: AsyncSession
    ) -> Optional[int]:
        db_charity_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charity_name
            )
        )
        return db_charity_id.scalars().first()


charity_project_crud = CRUDCharityProject(CharityProject)
