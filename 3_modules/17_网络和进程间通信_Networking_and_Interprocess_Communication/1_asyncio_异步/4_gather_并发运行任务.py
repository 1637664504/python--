import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def task(word,time):
    print('start ',word)
    await asyncio.sleep(time)
    print('end ',word)
    return True

async def main():
    # Schedule three calls *concurrently*:
    # L = await asyncio.gather(
    #     factorial("A", 2),
    #     factorial("B", 3),
    #     factorial("C", 4),
    # )
    print(L)
    N = await asyncio.gather(
        task('A',2),
        task('B',3),
        task('C',4),
    )
    print(N)

asyncio.run(main())

''' 
start  A
start  B
start  C
end  A
end  B
end  C
[True, True, True]
'''
