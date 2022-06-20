from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from FinalHW.utils.db_api.engine import create_session
from FinalHW.utils.db_api.models import Category

class CategoryCRUD(object):

    @staticmethod
    @create_session
    async def add(name: str, session: AsyncSession = None) -> int:
        category = Category(name=name)
        session.add(category)
        await session.refresh(category)
        return category.id

    @staticmethod
    @create_session
    async def get(category_id: int, session: AsyncSession = None) -> Category | None:
            # return session.get(Category, category_id)
        category = await session.execute(select(Category).where(Category.id == category_id))
        # return category.first()[0]

        # try:
        #     return category.first()[0]
        # except TypeError:
        #     return None

        if category := category.first():
            return category[0]

    @staticmethod
    @create_session
    async def delete(category_id: int, session: AsyncSession = None) -> None:
        await session.execute(delete(Category).where(Category.id == category_id))

    @staticmethod
    @create_session
    async def update(category_id: int, name: str = None, session: AsyncSession = None) -> None:
        await session.execute(update(Category).where(Category.id == category_id).values(
            name=name if name else Category.name
            )
        )




