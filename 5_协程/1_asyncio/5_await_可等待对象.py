import time
import asyncio

async def fun1():
    print("1111")
    await asyncio.sleep(2) #有了await 就是可等待对象
    print("fun1 end")

async def fun():
    print('----')
    # await fun1()

    await asyncio.sleep(3)

start_time = time.time()
asyncio.run(fun())
end_time = time.time()
print('spend time',end_time-start_time)