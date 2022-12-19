# app/core/db.py
from sqlalchemy import Integer, Column
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr
from app.core.config import settings


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.database_url)

# Create async func with sessionmaker for accessing the database
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


# Opening the session generator with coroutine
async def get_async_session():
    async with AsyncSession() as async_session:
        yield async_session
