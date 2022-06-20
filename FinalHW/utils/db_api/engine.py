from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import Session

DATABASE_URL: str = 'postgres:pgsandy567737@localhost:5432/onliner'

# engine = create_engine(f'postgresql+psycopg2://{DATABASE_URL}')
engine = create_async_engine(f'postgresql+asyncpg://{DATABASE_URL}')

# def create_session(func):
#     def wrapper(**kwargs):
#         with Session(bind=engine, autocommit=True) as session:
#             return func(**kwargs, session=session)
#     return wrapper

def create_session(func):
    async def wrapper(**kwargs):
        async with AsyncSession(bind=engine, autocommit=True) as session:
            return func(**kwargs, session=session)
    return wrapper