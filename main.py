import asyncio


async def loundary():
    print("Start washing")
    await asyncio.sleep(7)
    print("End washing")


async def soup():
    print("Start cooking")
    await asyncio.sleep(6)
    print("End cooking")


async def tea():
    print("Start boiling")
    await asyncio.sleep(1.5)
    print("End boiling")


async def sync_main():
    await loundary()
    await soup()
    await tea()


async def async_main():
    await asyncio.gather(loundary(), soup(), tea())

asyncio.run(async_main())
