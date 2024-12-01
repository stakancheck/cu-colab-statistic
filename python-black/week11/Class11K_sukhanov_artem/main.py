import asyncio
import os
from collections import defaultdict
from collections.abc import AsyncIterable

import aiofiles
from aiocsv import AsyncDictWriter, AsyncDictReader


class CSVReader:
    def __init__(self, file_path: str, chunk_size: int = 1024):
        self.file_path = file_path
        self.chunk_size = chunk_size
        self.headers = None

    async def read_in_chunks(self) -> AsyncIterable[list[dict[str, str]]]:
        async with aiofiles.open(self.file_path, mode='r') as file:
            reader = AsyncDictReader(file)
            self.headers = reader.fieldnames
            chunk = []
            async for row in reader:
                chunk.append(row)
                if len(chunk) >= self.chunk_size:
                    yield chunk
                    chunk = []
            if chunk:
                yield chunk

    @staticmethod
    def clean_review(review: dict[str, str]) -> dict[str, str]:
        stripped_review = {key: value.strip() for key, value in review.items()}
        if '||' in stripped_review['username']:
            better_name = stripped_review['username'].split('||')[0]
            better_name = better_name.capitalize()
            stripped_review['username'] = better_name
        return stripped_review


class GameDataProcessor:
    def __init__(self):
        self.game_data = defaultdict(list[dict[str, str]])

    def process_review(self, review: dict[str, str]):
        self.game_data[review['game_name']].append(review)

    def get_all_game_data(self) -> dict[str, list[dict[str, str]]]:
        return self.game_data


class GameFileWriter:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    async def save_game_data(self, game_name: str, reviews: list[dict[str, str]]):
        file_path = os.path.join(self.output_dir, f"{game_name}.csv")
        fieldnames: list[str] = list(reviews[0].keys())

        if not fieldnames:
            raise ValueError("No reviews found for game")

        async with aiofiles.open(file_path, mode='w', newline='') as file:
            writer = AsyncDictWriter(file, fieldnames=fieldnames)
            await writer.writeheader()
            for review in reviews:
                await writer.writerow(review)


class ReviewManager:
    csv_reader: CSVReader
    data_processor: GameDataProcessor
    file_writer: GameFileWriter

    def __init__(self, csv_path: str, output_dir: str, chunk_size: int = 10000):
        self.csv_reader = CSVReader(csv_path, chunk_size)
        self.data_processor = GameDataProcessor()
        self.file_writer = GameFileWriter(output_dir)

    async def process_reviews(self):
        async for chunk in self.csv_reader.read_in_chunks():
            for review in chunk:
                cleaned_review = self.csv_reader.clean_review(review)
                self.data_processor.process_review(cleaned_review)
            game_data = self.data_processor.get_all_game_data()
            for index, (game, reviews) in enumerate(game_data.items(), start=1):
                await self._write_game_data(game, reviews, index, len(game_data))

    async def _write_game_data(self, game: str, reviews: list[dict[str, str]], index: int, total_games: int):
        print(f"Writing data for '{game}' ({index} / {total_games})...")
        await self.file_writer.save_game_data(game, reviews)
        print(f"Complete '{game}' ({index} / {total_games})...")


async def main():
    review_manager = ReviewManager('steam_game_reviews.csv', 'output_data')
    await review_manager.process_reviews()


if __name__ == '__main__':
    asyncio.run(main())
