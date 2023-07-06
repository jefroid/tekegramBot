import aiohttp
import asyncio
url = 'https://api.thecatapi.com/v1/images/search?limit=10'
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def download(session: aiohttp.ClientSession,
                   url: str,
                   n: int):
    response = await session.get(url)
    response_bytes = await response.read()

    n += 1
    file = open(f'cats/cat{n}.jpg', 'wb')
    file.write(response_bytes)
    file.close()


async def main():
    session = aiohttp.ClientSession()

    response = await session.get(url)
    response_json = await response.json()

    url_cats = []
    for data in response_json:
        url_cats.append(data['url'])

    tasks = []
    for i in range(10):
        tasks.append(download(session, url_cats[i], i))
    await asyncio.gather(*tasks)

    response.release()

    await session.close()

def sync_main():
    asyncio.run(main())

sync_main()
