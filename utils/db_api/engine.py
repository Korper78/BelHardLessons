from sqlalchemy import create_engine
from sqlalchemy.orm import Session

DATABASE_URL: str = 'postgres:pgsandy567737@localhost:5432/shop'

engine = create_engine(f'postgresql+psycopg2://{DATABASE_URL}')

def create_session(func):
    def wrapper(**kwargs):
        with Session(bind=engine, autocommit=True) as session:
            return func(**kwargs, session=session)
    return wrapper