from aiohttp import ClientSession

def create_session(HOST):
    def wrap(func):
        async def called(**kwargs):
            async with ClientSession(base_url=HOST) as session:
                return await func(**kwargs, session=session)
        return called
    return wrap