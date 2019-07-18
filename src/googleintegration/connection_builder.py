from googleapiclient.discovery import build
from google.auth import default, iam
from google.auth.transport import requests
from google.oauth2 import service_account
from src.config import GOOGLE_API, ENV


def connect_to_api(api_name, api_version, scopes=None, subject=None):
    if ENV == 'test':
        return

    credentials, _ = default()
    credentials = __update_credentials(credentials, subject, scopes)

    return build(api_name, api_version, credentials=credentials, cache_discovery=False)


def __update_credentials(credentials, subject, scopes):
    try:
        updated_credentials = credentials.with_subject(subject).with_scopes(scopes)
    except AttributeError:
        # AttributeError implies that we are using GCE credentials so we cannot
        # use with_subject and with_scopes. Following link has more details:
        # https://github.com/GoogleCloudPlatform/professional-services/tree/master/examples/gce-to-adminsdk
        request = requests.Request()
        credentials.refresh(request)

        signer = iam.Signer(
            request,
            credentials,
            credentials.service_account_email
        )

        updated_credentials = service_account.Credentials(
            signer,
            credentials.service_account_email,
            GOOGLE_API['token_uri'],
            scopes=scopes,
            subject=subject
        )
    except Exception:
        raise

    return updated_credentials
