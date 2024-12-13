import os

from google_sheet_writer import GoogleSheetWriter
from youtube_parser import YouTubeParser
from youtube_scraper import YouTubeScraper


class YouTubeDataPipeline:
    def __init__(self, video_urls, spreadsheet_id):
        self.scraper = YouTubeScraper(video_urls)
        self.parser = YouTubeParser()
        self.writer = GoogleSheetWriter(
            spreadsheet_id=spreadsheet_id,
            worksheet_name=os.getenv('WORKSHEET_NAME', 'YouTube Data')
        )

    async def run(self):
        print("Starting YouTube data pipeline...")
        html_contents = await self.scraper.get_video_data()
        video_data = [self.parser.parse(html) for html in html_contents]
        self.writer.write_to_sheet(video_data)
        print("Pipeline completed!")
