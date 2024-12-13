import asyncio

import aiohttp


class YouTubeScraper:
    def __init__(self, video_urls):
        self.video_urls = video_urls

    @staticmethod
    async def fetch_html(url, session):
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                print(f"Successfully fetched HTML for {url}")
                return await response.text()
        except aiohttp.ClientError as e:
            print(f"Failed to fetch {url}: {e}")
            return None

    async def get_video_data(self):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            tasks = [self.fetch_html(url, session) for url in self.video_urls]
            return await asyncio.gather(*tasks)
