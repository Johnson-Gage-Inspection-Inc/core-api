from _typeshed import Incomplete
from office365.runtime.auth.authentication_provider import AuthenticationProvider as AuthenticationProvider

class NetworkCredentialProvider(AuthenticationProvider):
    userCredentials: Incomplete
    def __init__(self, username, password) -> None: ...
    def authenticate_request(self, request) -> None: ...
