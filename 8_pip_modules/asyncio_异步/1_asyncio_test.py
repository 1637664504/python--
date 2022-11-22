import asyncio
import time

async def counter_loop(x, n):
    for i in range(1, n + 1):
        print(f"Counter {x}: {i}")
        await asyncio.sleep(1)
        # time.sleep(1)
    #return f"Finished {x} in {n}"

async def main():
    slow_task = asyncio.create_task(counter_loop("Slow", 4))
    # fast_coro = asyncio.create_task(counter_loop("Fast", 2))
    fast_coro = counter_loop("Fast", 8)

    print("Awaiting Fast")
    await fast_coro
    print("Finished Fast") 

    print("Awaiting Slow")
    await slow_task
    print("Finished Slow")

    #print(f"{fast_val}, {slow_val}")

asyncio.run(main())