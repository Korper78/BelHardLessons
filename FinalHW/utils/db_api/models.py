from sqlalchemy import Column, SmallInteger, VARCHAR, DECIMAL, ForeignKey, INT
from sqlalchemy.orm import declarative_base

OnlinerBase = declarative_base()

class Category(OnlinerBase):
    __tablename__: str = 'categories'
    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False, unique=True)
    # parent_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'))
    # descr = Column(VARCHAR(140), nullable=False)
# CREATE TABLE categories(id SERIAL PRIMARY KEY, name VARCHAR(20) UNIQUE NOT NULL);

class Product(OnlinerBase):
    __tablename__: str = 'products'
    id = Column(INT, primary_key=True)
    key = Column(VARCHAR(20), nullable=False, unique=True)
    full_name = Column(VARCHAR(60), nullable=False)
    category_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    page = Column(INT, nullable=False)
    on_page = Column(SmallInteger, nullable=False)
    # description = Column(VARCHAR(140))
    # price = Column(DECIMAL(8, 2), nullable=False)
# CREATE TABLE products(id SERIAL PRIMARY KEY, key VARCHAR(20) UNIQUE NOT NULL, full_name VARCHAR(60) NOT NULL, category_id INTEGER NOT NULL REFERENCES categories(id), page INTEGER NOT NULL, on_page SMALLINT NOT NULL);
