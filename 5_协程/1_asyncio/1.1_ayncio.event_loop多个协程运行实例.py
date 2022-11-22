# python 源码
import asyncio


async def func1():
    print('协程1')

async def func2():
    print('协程2')

# task可为列表,即任务列表
# task = func1()
task = [func1(), func2()]
# 创建事件循环
loop = asyncio.get_event_loop()
# 添加任务，直至所有任务执行完成
loop.run_until_complete(asyncio.wait(task))
#关闭事件循环
loop.close()
# 事件循环关闭后，再次调用loop，将不会再次执行。
