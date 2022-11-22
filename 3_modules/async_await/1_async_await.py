import time
async def funa():
    print("111")
    time.sleep(10)
    print("222")

async def funb():
    print("333")

await funa()
await funb()
