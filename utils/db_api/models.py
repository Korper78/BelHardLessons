from sqlalchemy import Column, SmallInteger, VARCHAR, DECIMAL, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__: str = 'categories'
    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False)
    parent_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'))
    # descr = Column(VARCHAR(140), nullable=False)

class Product(Base):
    __tablename__: str = 'products'
    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    description = Column(VARCHAR(140))
    price = Column(DECIMAL(8, 2), nullable=False)
    category_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)

