from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account

class sheets_api:
    def __init__(self, cred_json, sheet_id):
        """Sets up access to spreadsheet.
        """
        self.creds = service_account.Credentials.from_service_account_file(
                cred_json,
                scopes=['https://www.googleapis.com/auth/spreadsheets'])
        self.spreadsheet_id = sheet_id

    def read(self, tab_name):
        """Reads spreadsheet with name tab_name & returns values array.
        """
        service = build('sheets', 'v4', credentials=self.creds)
        self.sheet = service.spreadsheets()
        result = self.sheet.values().get(spreadsheetId=self.spreadsheet_id,
                range="{}".format(tab_name)).execute()
        values = result.get('values', [])
        return values

    def write(self, tab_name, input_array):
        """Writes input_array (2d array) to spreadsheet tab_name.
        """
        request = self.sheet.values().update(spreadsheetId=self.spreadsheet_id,
                range="{}".format(tab_name),
                valueInputOption="USER_ENTERED",
                body={"values":input_array}).execute()
        return
