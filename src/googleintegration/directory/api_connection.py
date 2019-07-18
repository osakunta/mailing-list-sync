from src.googleintegration.connection_builder import connect_to_api
from src.config import GOOGLE_API


def __create_api_connection():
    return connect_to_api(
        'admin',
        'directory_v1',
        scopes=GOOGLE_API['directory_scopes'],
        subject=GOOGLE_API['delegated_user']
    )


service = __create_api_connection()
