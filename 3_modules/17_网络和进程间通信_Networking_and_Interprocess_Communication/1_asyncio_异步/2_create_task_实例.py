import asyncio

async def task(word,time):
    print('start ',word)
    await asyncio.sleep(time)
    print('end ',word)


async def main():
    task1 = asyncio.create_task(task('hello',2))
    task2 = asyncio.create_task(task('world',3))
    # await task1,task2
    await task1
    await task2

asyncio.run(main())

''' 
测试1:
await task1,task2
time: 2s

'''

''' 
测试2
    await task1
    await task2

time: 3s

'''