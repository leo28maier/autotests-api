import asyncio

import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Receive message:{message}")
        response = f"Server response:{message}"
        await websocket.send(response)


async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Server listening on port 8765")
    await server.wait_closed()

asyncio.run(main())