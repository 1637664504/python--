# python 源码
import asyncio

async def main():
    print('hello')
    # asyncio.sleep(1)          #异步函数,time = 0.048s
    await asyncio.sleep(1)      #等等异步函数完成, time= 1.040s

    print('world')

asyncio.run(main())