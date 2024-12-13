import asyncio
import json
from datetime import datetime
from time import perf_counter

import aiofiles
import websockets

connected_clients = set()

async def log_message(client_id, message, sender):
    log_entry = {
        'time': datetime.now().isoformat(),
        'client_id': client_id,
        'message': message,
        'sender': sender
    }
    async with aiofiles.open('messages.json', mode='a') as file:
        await file.write(json.dumps(log_entry, ensure_ascii=False) + '\n')

async def handle_client(websocket):
    client_id = f"Client_{len(connected_clients) + 1}"
    connected_clients.add(websocket)
    await websocket.send("Добро пожаловать в чат!")
    await log_message(client_id, "Добро пожаловать в чат!", "server")

    try:
        async for message in websocket:
            await log_message(client_id, message, "client")
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.ConnectionClosed:
        await log_message(client_id, "Сессия завершена. До свидания!", "server")
    finally:
        connected_clients.remove(websocket)
        await websocket.close()

async def main():
    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
