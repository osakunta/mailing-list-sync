from src.googleintegration.connection_builder import connect_to_api
from src.config import GOOGLE_API


def __create_api_connection():
    return connect_to_api(
        'sheets',
        'v4',
        scopes=GOOGLE_API['sheets_scopes']
    )


service = __create_api_connection()
