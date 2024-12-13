import asyncio
import websockets
import json


class RockPaperScissorsGame:
    """
    Класс для управления игрой "Камень-Ножницы-Бумага" между двумя игроками.

    Атрибуты:
        player1_ws (websockets.WebSocketServerProtocol): WebSocket для Игрока 1.
        player2_ws (websockets.WebSocketServerProtocol): WebSocket для Игрока 2.
        players (dict): Словарь, связывающий соединения WebSocket с их ходами.
        game_over (bool): Флаг, указывающий, завершена ли игра.
    """

    def __init__(self, player1_ws, player2_ws):
        """
        Инициализирует игру с двумя соединениями WebSocket для игроков.

        Аргументы:
            player1_ws (websockets.WebSocketServerProtocol): WebSocket для Игрока 1.
            player2_ws (websockets.WebSocketServerProtocol): WebSocket для Игрока 2.
        """
        self.players = {
            player1_ws: None,
            player2_ws: None,
        }  # Хранит ходы для каждого игрока
        self.player1_ws = player1_ws
        self.player2_ws = player2_ws
        self.game_over = False  # Флаг состояния игры

    async def receive_move(self, websocket):
        """
        Получает ход от игрока.

        Аргументы:
            websocket (websockets.WebSocketServerProtocol): Соединение WebSocket игрока.

        Возвращает:
            bool: True, если ход действителен и получен, иначе False.
        """
        try:
            data = await websocket.recv()  # Получает данные от игрока
            message = json.loads(data)  # Парсит JSON сообщение
            move = message.get("move")  # Извлекает ход
            if move not in ["rock", "paper", "scissors"]:
                # Отправляет сообщение об ошибке, если ход недействителен
                await websocket.send(
                    json.dumps({"type": "error", "message": "Недопустимый ход"})
                )
                return False
            self.players[websocket] = move  # Сохраняет ход игрока
            return True
        except websockets.exceptions.ConnectionClosed:
            # Обрабатывает случай, когда игрок отключается
            print("Соединение закрыто")
            return False

    async def determine_winner(self):
        """
        Определяет победителя на основе ходов игроков и отправляет результат.
        """
        move1 = self.players[self.player1_ws]
        move2 = self.players[self.player2_ws]
        result = self.get_result(move1, move2)
        # Отправляет результат обоим игрокам
        await self.broadcast(
            {"type": "result", "move1": move1, "move2": move2, "result": result}
        )
        self.game_over = True  # Устанавливает флаг завершения игры

    def get_result(self, move1, move2):
        """
        Определяет результат игры на основе традиционных правил "Камень-Ножницы-Бумага".

        Аргументы:
            move1 (str): Ход Игрока 1.
            move2 (str): Ход Игрока 2.

        Возвращает:
            str: 'player1', если побеждает Игрок 1; 'player2', если побеждает Игрок 2; 'draw', если ничья.
        """
        if move1 == move2:
            return "draw"
        # Определяет, какой ход побеждает
        wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
        if wins[move1] == move2:
            return "player1"
        else:
            return "player2"

    async def broadcast(self, message):
        """
        Отправляет сообщение обоим игрокам.

        Аргументы:
            message (dict): Сообщение для отправки.
        """
        await self.player1_ws.send(json.dumps(message))
        await self.player2_ws.send(json.dumps(message))


async def handler(websocket):
    """
    Обрабатывает входящие WebSocket соединения.

    Аргументы:
        websocket (websockets.WebSocketServerProtocol): Соединение WebSocket игрока.
    """
    print("Новое соединение")
    try:
        # Если есть игрок, ожидающий соперника, начинается новая игра
        if waiting_players:
            opponent_ws = waiting_players.pop(0)
            game = RockPaperScissorsGame(opponent_ws, websocket)
            await start_game(game)
        else:
            # В противном случае добавляем этого игрока в список ожидания
            waiting_players.append(websocket)
            await websocket.send(
                json.dumps({"type": "waiting", "message": "Ожидание соперника..."})
            )
            # Поддерживаем соединение открытым во время ожидания
            await websocket.wait_closed()
    except websockets.exceptions.ConnectionClosed:
        # Обрабатывает отключение
        print("Соединение закрыто")
    finally:
        # Очистка, если игрок отключился
        if websocket in waiting_players:
            waiting_players.remove(websocket)


async def start_game(game):
    """
    Отправляет сообщения о начале игры обоим игрокам и запускает игровой цикл.

    Аргументы:
        game (RockPaperScissorsGame): Экземпляр игры.
    """
    # Уведомляет игроков, что игра началась
    await game.player1_ws.send(
        json.dumps(
            {
                "type": "start",
                "player": "player1",
                "message": "Игра началась. Вы - Игрок 1",
            }
        )
    )
    await game.player2_ws.send(
        json.dumps(
            {
                "type": "start",
                "player": "player2",
                "message": "Игра началась. Вы - Игрок 2",
            }
        )
    )
    # Запускает игровой цикл
    await game_loop(game)


async def game_loop(game):
    """
    Основной игровой цикл для обработки ходов и определения победителя.

    Аргументы:
        game (RockPaperScissorsGame): Экземпляр игры.
    """
    while not game.game_over:
        # Запрашивает у обоих игроков ввод ходов
        await game.player1_ws.send(
            json.dumps(
                {
                    "type": "your_move",
                    "message": "Введите ваш ход (камень, ножницы или бумага):",
                }
            )
        )
        await game.player2_ws.send(
            json.dumps(
                {
                    "type": "your_move",
                    "message": "Введите ваш ход (камень, ножницы или бумага):",
                }
            )
        )

        # Одновременный приём ходов от обоих игроков
        receive_moves = [
            game.receive_move(game.player1_ws),
            game.receive_move(game.player2_ws),
        ]
        results = await asyncio.gather(*receive_moves)

        # Если любой игрок сделал недопустимый ход или отключился, завершает игру
        if not all(results):
            await game.broadcast(
                {
                    "type": "error",
                    "message": "Игрок отключился или сделал недопустимый ход.",
                }
            )
            break

        # Определяет победителя и отправляет результат
        await game.determine_winner()
        break  # Завершает игру после одного раунда


# Список для отслеживания игроков, ожидающих соперника
waiting_players = []


async def main():
    """
    Основная функция для запуска сервера и прослушивания соединений.
    """
    async with websockets.serve(handler, "localhost", 6789):
        print("Сервер запущен на ws://localhost:6789")
        await asyncio.Future()  # Поддерживает работу сервера


if __name__ == "__main__":
    # Запуск сервера
    asyncio.run(main())
