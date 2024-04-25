from starlette.config import Config
from authlib.integrations.starlette_client import OAuth

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

oauth2 = OAuth(config)

oauth2.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile',
        'prompt': 'select_account',  # force to select account
    }
)