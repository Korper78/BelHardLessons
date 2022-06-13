from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from utils.db_api.engine import create_session
from utils.db_api.models import Product


class ProductCRUD(object):

    @staticmethod
    @create_session
    def add(name: str, description: str = '', price: float = 0.0, category_id: int = 1, session: Session = None) -> int:
        product = Product(name=name, description=description, price=price, category_id=category_id)
        session.add(product)
        session.refresh(product)
        return product.id

    @staticmethod
    @create_session
    def get(product_id: int, session: Session = None) -> Product | None:
        product = session.execute(select(Product).where(Product.id == product_id))
        # return category.first()[0]

        # try:
        #     return category.first()[0]
        # except TypeError:
        #     return None

        if product := product.first():
            return product[0]

    @staticmethod
    @create_session
    def delete(product_id: int, session: Session = None) -> None:
        session.execute(delete(Product).where(Product.id == product_id))

    @staticmethod
    @create_session
    def update(product_id: int, name: str = None, description: str = '',
               price: float = None, category_id: int = None, session: Session = None) -> None:
        session.execute(update(Product).where(Product.id == product_id).values(
            name=name if name else Product.name,
            description=description if description else Product.description,
            price=price if price else Product.price,
            category_id=category_id if category_id else Product.category_id
            )
        )
