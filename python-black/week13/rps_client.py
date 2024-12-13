import asyncio
import websockets
import json


async def play():
    """
    Подключиться к серверу и сыграть в игру.
    """
    uri = "ws://localhost:6789"  # Адрес сервера
    async with websockets.connect(uri) as websocket:
        player = None  # Будет содержать 'player1' или 'player2'
        while True:
            try:
                data = await websocket.recv()  # Получить данные от сервера
                message = json.loads(data)  # Парсить JSON сообщение

                # Обработка сообщений в зависимости от их типа
                if message["type"] == "waiting":
                    # Ожидание соперника
                    print(message["message"])
                elif message["type"] == "start":
                    # Игра началась
                    player = message["player"]
                    print(message["message"])
                elif message["type"] == "your_move":
                    # Ход игрока
                    print(message["message"])
                    move = input().strip().lower()  # Получить ввод от пользователя
                    # Отправить ход на сервер
                    await websocket.send(json.dumps({"move": move}))
                elif message["type"] == "result":
                    # Получить результат игры
                    move1 = message["move1"]
                    move2 = message["move2"]
                    result = message["result"]
                    print(f"Игрок 1 выбрал: {move1}")
                    print(f"Игрок 2 выбрал: {move2}")
                    if result == "draw":
                        print("Ничья!")
                    elif (result == "player1" and player == "player1") or (
                        result == "player2" and player == "player2"
                    ):
                        print("кто-то выиграл")
                    break  # Выйти из цикла после завершения игры
                elif message["type"] == "error":
                    # Обработка ошибок, отправленных сервером
                    print("Ошибка:", message["message"])
                    break
                else:
                    # Обработка неожиданных сообщений
                    print("Неизвестное сообщение:", message)
            except websockets.exceptions.ConnectionClosed:
                # Обработка отключения
                print("Соединение закрыто")
                break


if __name__ == "__main__":
    # Запуск клиента
    asyncio.run(play())
