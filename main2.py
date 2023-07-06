from random import random
import asyncio


async def kitty(n):
    print("downloading cat", n)
    await asyncio.sleep(random()+1)
    print(n, "cat downloaded")


async def async_main():
    await asyncio.gather(kitty(1), kitty(2), kitty(3), kitty(4), kitty(5), kitty(6), kitty(7), kitty(8), kitty(9), kitty(10))

asyncio.run(async_main())
