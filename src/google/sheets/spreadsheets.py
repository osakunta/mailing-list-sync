from src.google.sheets.api_connection import service
from src.utils import flatten


def get(spreadsheet_id, range):
    request = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=range,
    )

    response = request.execute()
    values = flatten(response.get('values', []))

    return values
