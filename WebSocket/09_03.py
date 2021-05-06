import asyncio 

async def async_func1():
    print("Hello")


# 때에 따라 이벤트 루프 동작 등을 세부적으로 제어할 필요가 있을 수 있습니다. 
# 이럴 때는 다음과 같이 프로그래머가 직접 이벤트 루프를 얻고 이벤트 루프를 통해 
# 코루틴을 처리한 후 이벤트 루프를 닫을 수 있습니다.
loop = asyncio.get_event_loop()
loop.run_until_complete(async_func1())
loop.close()