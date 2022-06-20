import asyncio

from FinalHW.utils.url_api.api_engine import create_session
from FinalHW.utils.url_api.jsnmodels import OnlinerResponse
from aiohttp import ClientSession
# from asyncio import run


class OnlinerAPI(object):
    HOST: str = 'https://catalog.onliner.by'

    @staticmethod
    @create_session(HOST)
    async def onliner_get(category: str, session: ClientSession = None) -> OnlinerResponse | None:
        # response = await session.get(url=f'{OnlinerAPI.HOST}/sdapi/catalog.api/search/{category}')
        response = await session.get(url=f'/sdapi/catalog.api/search/{category}')
        if response.status == 200:
            # return OnlinerResponse(response.json())
            resp_dict = await response.json()
            return OnlinerResponse(**resp_dict)
        else:
            return None


async def main():
    onliner = await OnlinerAPI.onliner_get(category='notebook?page=1')
    # _onliner = OnlinerResponse(**onliner)
    print(onliner)

if __name__ == '__main__':
    asyncio.run(main())
    # onliner = await OnlinerAPI.onliner_get(category='notebook?page=1')
    # _onliner = OnlinerResponse(**onliner)
