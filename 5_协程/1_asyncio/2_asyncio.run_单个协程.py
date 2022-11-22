import time
import asyncio

async def fun():
    print("start washer")
    time.sleep(3)  # 第一台洗衣机,
    print('washer1 finished')  # 洗完了

# 方法1: 直接运行
asyncio.run(fun())

# 方法2: 使用变量的方式
# coroutine_1 = fun()  # 协程是一个对象，不能直接运行
# asyncio.run(coroutine_1)