import requests
import asyncio


async def downloadCat(name, url):
    name = 'cat' + name + url[len(url)-4: len(url)]
    file = open(name, 'wb')
    file.write(requests.get(url).content)
    file.close()


async def main():
    a = []
    catAPIUrl = 'https://api.thecatapi.com/v1/images/search?limit=10'
    response = eval(requests.get(catAPIUrl).text)
    response = requests.get(catAPIUrl).json()
    for i in range(10):
        a.append(response[i]['url'])
    await asyncio.gather(downloadCat('1', a[0]), downloadCat('2', a[1]), downloadCat('3', a[2]), downloadCat('4', a[3]), downloadCat('5', a[4]), downloadCat('6', a[5]),
                         downloadCat('7', a[6]), downloadCat('8', a[7]), downloadCat('9', a[8]), downloadCat('10', a[9]))

asyncio.run(main())
