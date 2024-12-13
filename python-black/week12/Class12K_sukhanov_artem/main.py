import asyncio
import os

from dotenv import load_dotenv

from youtube_data_pipeline import YouTubeDataPipeline

load_dotenv()


async def main():
    video_urls = [
        'https://www.youtube.com/watch?v=NSDdJeCmXXE',
        'https://www.youtube.com/watch?v=WGsMydFFPMk'
    ]
    spreadsheet_id = os.getenv('SPREADSHEET_ID')

    pipeline = YouTubeDataPipeline(video_urls, spreadsheet_id)
    await pipeline.run()


if __name__ == "__main__":
    asyncio.run(main())
