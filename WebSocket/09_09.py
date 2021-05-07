import websockets
import asyncio 
import json

async def bithumb_ws_client():
    uri = "wss://pubwss.bithumb.com/pub/ws"

    async with websockets.connect(uri, ping_interval=None) as websocket:
        greeting = await websocket.recv()
        print(greeting)

        subscribe_fmt = {
            "type":"ticker", 
            "symbols": ["BTC_KRW"], 
            "tickTypes": ["1H"]
        }
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            print(data)


async def main():
    await bithumb_ws_client()

asyncio.run(main())

# json 모듈을 사용해서 파이썬 딕셔너리를 JSON 타입으로 변환
# 구독 요청을 서버에 전송
# while 문으로 무한 루프를 생성
# 빗썸 서버로부터 데이터를 받기
# 전달받은 JSON 타입의 데이터를 파이썬 딕셔너리 타입으로 변환
# 딕셔너리 출력