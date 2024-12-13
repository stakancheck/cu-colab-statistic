import aiohttp
import asyncio


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientError as e:
            print(f"Request failed: {e}")
            return None


async def fetch_all_reviews(urls):
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    reviews = [review for result in results if result for review in result]
    return reviews
