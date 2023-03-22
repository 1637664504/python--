import asyncio

async def eternity():
    # Sleep for 6s
    await asyncio.sleep(6)
    print('yay!')

async def main():
    task = asyncio.create_task(eternity())
    try:
        await asyncio.shield(task)
    except asyncio.TimeoutError:
        print('timeout!')


asyncio.run(main())
