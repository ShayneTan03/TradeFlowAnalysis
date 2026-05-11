import asyncio
import websockets
import json
import os

load_dotenv()

async def connect_aisstream():
    async with websockets.connect("wss://stream.aisstream.io/v0/stream") as websocket:
        subscribe_message = {
            "APIKey": os.getenv("AISSTREAM_API_KEY"),
            "BoundingBoxes": [[[-90,-180], [90,180]]],
        }
        await websocket.send(json.dumps(subscribe_message))

        async for message in websocket:
            ais_message = json.loads(message)
            print(ais_message)
asyncio.run(connect_aisstream())