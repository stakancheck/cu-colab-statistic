import aiofiles
import json


async def save_reviews(reviews, filename='reviews.json'):
    async with aiofiles.open(filename, 'w') as file:
        await file.write(json.dumps(reviews, ensure_ascii=False, indent=4))
