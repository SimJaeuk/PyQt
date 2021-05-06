import asyncio

async def async_func1():
    print("Hello")

#async_func1()
#코루틴의 실행에는 항상 이벤트 루프가 필요하다.
asyncio.run(async_func1())
