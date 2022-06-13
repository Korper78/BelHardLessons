from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from utils.db_api.engine import create_session
from utils.db_api.models import Category

class CategoryCRUD(object):

    @staticmethod
    @create_session
    def add(name: str, parent_id: int = None, session: Session = None) -> int:
        category = Category(name=name, parent_id=parent_id)
        session.add(category)
        session.refresh(category)
        return category.id

    @staticmethod
    @create_session
    def get(category_id: int, session: Session = None) -> Category | None:
            # return session.get(Category, category_id)
        category = session.execute(select(Category).where(Category.id == category_id))
        # return category.first()[0]

        # try:
        #     return category.first()[0]
        # except TypeError:
        #     return None

        if category := category.first():
            return category[0]

    @staticmethod
    @create_session
    def delete(category_id: int, session: Session = None) -> None:
        session.execute(delete(Category).where(Category.id == category_id))

    @staticmethod
    @create_session
    def update(category_id: int, name: str = None, parent_id: int = None, session: Session = None) -> None:
        session.execute(update(Category).where(Category.id == category_id).values(
            name=name if name else Category.name,
            parent_id=parent_id if parent_id else Category.parent_id
            )
        )




