import asyncio

from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosedOK

async def handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)

async def main():
    async with serve(handler, "", 8001) as server:
        await server.serve_forever()

async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
        except ConnectionClosedOK:
            break
            print(message)

if __name__ == "__main__":
    asyncio.run(main())