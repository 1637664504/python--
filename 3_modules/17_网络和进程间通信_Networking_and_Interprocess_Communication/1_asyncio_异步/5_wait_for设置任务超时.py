import asyncio

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(6)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')
    
    #报错 TimeoutError
    # await asyncio.wait_for(eternity(), timeout=1.0)

asyncio.run(main())
