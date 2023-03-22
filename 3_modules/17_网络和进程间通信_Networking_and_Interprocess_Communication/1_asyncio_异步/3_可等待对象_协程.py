import asyncio
import time

async def nested():
    print('1111')
    time.sleep(2)
    print('2222')
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".
    time.sleep(10)

asyncio.run(main())