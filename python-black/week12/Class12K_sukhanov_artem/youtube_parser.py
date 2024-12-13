from bs4 import BeautifulSoup


class YouTubeParser:
    @staticmethod
    def parse(html_content):
        if not html_content:
            print("No HTML content to parse")
            return {}

        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            video_data = {
                'title': soup.find('meta', attrs={'name': 'title'})['content'],
                'description': soup.find('meta', attrs={'name': 'description'})['content'],
                'tags': [tag['content'] for tag in soup.find_all('meta', property='og:video:tag')],
                'channel_name': soup.find('link', itemprop='name')['content'],
                'views_number': soup.find('meta', itemprop='interactionCount')['content'],
                'upload_date': soup.find('meta', itemprop='uploadDate')['content'],
                'genre': soup.find('meta', itemprop='genre')['content']
            }
            print("Successfully parsed video data")
            return video_data
        except Exception as e:
            print(f"Error parsing HTML content: {e}")
            return {}
