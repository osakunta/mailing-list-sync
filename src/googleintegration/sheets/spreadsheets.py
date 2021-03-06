from src.googleintegration.sheets.api_connection import service
from src.utils import flatten


def get(spreadsheet_id, value_range):
    request = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=value_range,
    )

    response = request.execute()
    values = flatten(response.get('values', []))

    return values
