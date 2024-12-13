import asyncio
import websockets

async def listen_for_messages(websocket):
    async for message in websocket:
        print(f"\n{message}")

async def send_messages(websocket):
    while True:
        message = await asyncio.get_event_loop().run_in_executor(None, input, "\nEnter message: ")
        await websocket.send(message)

async def main():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await asyncio.gather(
            listen_for_messages(websocket),
            send_messages(websocket)
        )

if __name__ == "__main__":
    asyncio.run(main())
