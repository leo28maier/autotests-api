import asyncio

import websockets

async def client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        message = "Hi Server"
        print(f"Sending message: {message}")
        await websocket.send(message)

        response = await websocket.recv()
        print(f"Received response: {response}")


asyncio.run(client())