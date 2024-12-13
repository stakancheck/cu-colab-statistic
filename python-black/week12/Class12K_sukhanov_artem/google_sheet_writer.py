import os

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheetWriter:
    def __init__(self, spreadsheet_id, worksheet_name='YouTube Data'):
        self.spreadsheet_id = spreadsheet_id
        self.worksheet_name = worksheet_name
        self.sheet = None
        self.range = f"{worksheet_name}!A1"

    @staticmethod
    def get_service_sacc():
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        keyfile = os.getenv('GOOGLE_SHEET_CREDENTIALS_JSON')

        if not keyfile:
            raise ValueError("GOOGLE_SHEET_CREDENTIALS_JSON environment variable is not set.")
        if not os.path.exists(keyfile):
            raise FileNotFoundError(f"Credentials file not found: {keyfile}")

        creds_service = ServiceAccountCredentials.from_json_keyfile_name(
            os.getenv('GOOGLE_SHEET_CREDENTIALS_JSON'),
            scope
        ).authorize(httplib2.Http())
        return build('sheets', 'v4', http=creds_service)

    def init_spreadsheet(self):
        service = self.get_service_sacc()
        self.sheet = service.spreadsheets()

    def write_to_sheet(self, data):
        if not self.sheet:
            self.init_spreadsheet()

        for video in data:
            resp = self.sheet.values().append(
                spreadsheetId=self.spreadsheet_id,
                range=self.range,
                valueInputOption='RAW',
                body={
                    'values': [
                        [
                            video.get('title', ''),
                            video.get('description', ''),
                            ', '.join(video.get('tags', [])),
                            video.get('channel_name', ''),
                            video.get('views_number', ''),
                            video.get('upload_date', ''),
                            video.get('genre', '')
                        ]
                    ]
                }
            ).execute()

            print(f"Data writing to sheet response: {resp}")

        print("Data written to sheet.")
