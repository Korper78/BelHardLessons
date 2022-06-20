import asyncio

from FinalHW.utils.url_api.OnlinerAPI import OnlinerAPI
from FinalHW.utils.url_api.FastAPIutils import FastAPI
from FinalHW.utils.url_api.jsnmodels import PostRequest


async def main():
    choice = input('Выберите:\n<1> Ввести с клавиатуры\n<2> Запросить с API\n>>>')
    # print(choice)
    match choice:
        case '1':
            category = input('Введите название категории>>>')
            product = input('Введите артикул товара>>>')
            page, on_page = 1, -1
            while True:
                response = await OnlinerAPI.onliner_get(category=f'{category.lower()}?page={page}')
                if response:
                    try:
                        on_page = [x.key for x in response.products].index(product)
                        break
                    except ValueError:
                        page += 1
                else:
                    break
            if on_page >= 0:
                print(f'Товар категории {category} с артикулом {product} найден на странице {page} под номером {on_page} и называется {response.products[on_page].full_name}')
            else:
                print(f'Товар категории {category} с артикулом {product} не найден в Каталоге Онлайнер')
        case '2':
            api_resp = await FastAPI.fastapi_get()
            # print(api_resp)
            # category = input('Введите название категории>>>')
            # product = input('Введите артикул товара>>>')
            on_page = -1
            for page in range(1, api_resp.depth+1):
                response = await OnlinerAPI.onliner_get(category=f'{api_resp.category}?page={page}')
                try:
                    on_page = [x.key for x in response.products].index(api_resp.key)
                    break
                except ValueError:
                    continue
            if on_page>= 0:
                print(f'Товар категории {api_resp.category} с артикулом {api_resp.key} найден на странице {page} под номером {on_page} и называется {response.products[on_page].full_name}')
                api_req = PostRequest(**{
                    'key': api_resp.key,
                    'page': page,
                    'id': on_page
                })
                # api_req.key = api_resp.key
                # api_req.page = page
                # api_req.id = on_page
                await FastAPI.fastapi_post(req=api_req)
            else:
                print(f'Товар категории {api_resp.category} с артикулом {api_resp.key} не найден на страницах до {page}')

        case _:
            print('Invalid choice')



if __name__ == '__main__':
    asyncio.run(main())