from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from FinalHW.utils.db_api.engine import create_session
from FinalHW.utils.db_api.models import Product


class ProductCRUD(object):

    @staticmethod
    @create_session
    def add(key: str, full_name: str, category_id: int = 1,
            page: int = 1, on_page: int = 1, session: AsyncSession = None) -> int:
        product = Product(
            key=key,
            full_name=full_name,
            category_id=category_id,
            page=page,
            on_page=on_page
        )
        session.add(product)
        await session.refresh(product)
        return product.id

    @staticmethod
    @create_session
    def get(key: str, session: AsyncSession = None) -> Product | None:
        product = await session.execute(select(Product).where(Product.key == key))
        # return category.first()[0]

        # try:
        #     return category.first()[0]
        # except TypeError:
        #     return None

        if product := product.first():
            return product[0]

    @staticmethod
    @create_session
    def delete(key: str, session: AsyncSession = None) -> None:
        await session.execute(delete(Product).where(Product.key == key))

    @staticmethod
    @create_session
    def update(product_id: int, key: str = None, full_name: str = None, category_id: int = None,
               page: int = None, on_page: int = None, session: AsyncSession = None) -> None:
        await session.execute(update(Product).where(Product.id == product_id).values(
            key=key if key else Product.key,
            full_name=full_name if full_name else Product.full_name,
            category_id=category_id if category_id else Product.category_id,
            page=page if page else Product.page,
            on_page=on_page if on_page else Product.on_page
            )
        )
