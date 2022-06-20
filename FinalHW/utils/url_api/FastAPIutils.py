import asyncio

from FinalHW.utils.url_api.api_engine import create_session
from FinalHW.utils.url_api.jsnmodels import GetResponse, PostRequest
from aiohttp import ClientSession
# from asyncio import run

class FastAPI(object):
    HOST: str = 'https://4b9a-178-127-105-234.eu.ngrok.io'

    @staticmethod
    @create_session(HOST)
    async def fastapi_get(session: ClientSession = None) -> GetResponse | None:
        # response = await session.get(url=f'{OnlinerAPI.HOST}/sdapi/catalog.api/search/{category}')
        response = await session.get(url='/')
        if response.status == 200:
            # return OnlinerResponse(response.json())
            resp_dict = await response.json()
            return GetResponse(**resp_dict)
        else:
            return None

    @staticmethod
    @create_session(HOST)
    async def fastapi_post(req: PostRequest,session: ClientSession = None) -> None:
        # response = await session.get(url=f'{OnlinerAPI.HOST}/sdapi/catalog.api/search/{category}')
        await session.post(url='/add', data=dict(req))
        # if response.status == 200:
        #     # return OnlinerResponse(response.json())
        #     return await response.json()
        # else:
        #     return {"Response": response.status}

async def main():
    onliner = await FastAPI.fastapi_get()
    # _onliner = GetResponse(**onliner)
    print(onliner)

if __name__ == '__main__':
    asyncio.run(main())
    # onliner = await OnlinerAPI.onliner_get(category='notebook?page=1')
    # _onliner = OnlinerResponse(**onliner)

