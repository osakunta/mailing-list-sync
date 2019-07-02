from src.google.sheets.api_connection import service


def get(spreadsheet_id, range):
    request = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=range,
    )

    response = request.execute()

    return response
