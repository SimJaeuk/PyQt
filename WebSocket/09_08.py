import websockets
import asyncio

async def bithumb_ws_client():
    uri = "wss://pubwss.bithumb.com/pub/ws"
    
    async with websockets.connect(uri) as websocket:
        greeting = await websocket.recv()
        print(greeting)

async def main():
    await bithumb_ws_client()

asyncio.run(main())

# 빗썸 웹소켓 서버에 연결 후
# 서버로부터 데이터를 받아서 출력