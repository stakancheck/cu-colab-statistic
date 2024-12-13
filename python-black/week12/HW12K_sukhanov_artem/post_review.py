import aiohttp


async def post_new_review(url, review):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, json=review) as response:
                response.raise_for_status()
                print("Review posted successfully")
        except aiohttp.ClientError as e:
            print(f"Failed to post review: {e}")
