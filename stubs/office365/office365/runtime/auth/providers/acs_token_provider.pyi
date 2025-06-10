import office365.logger
from _typeshed import Incomplete
from office365.azure_env import AzureEnvironment as AzureEnvironment
from office365.runtime.auth.authentication_provider import (
    AuthenticationProvider as AuthenticationProvider,
)
from office365.runtime.auth.token_response import TokenResponse as TokenResponse
from office365.runtime.compat import urlparse as urlparse
from office365.runtime.http.request_options import RequestOptions as RequestOptions

class ACSTokenProvider(AuthenticationProvider, office365.logger.LoggerContext):
    url: Incomplete
    redirect_url: Incomplete
    error: Incomplete
    SharePointPrincipal: str
    def __init__(
        self, url, client_id, client_secret, environment: Incomplete | None = None
    ) -> None: ...
    def authenticate_request(self, request: RequestOptions) -> None: ...
    def get_app_only_access_token(self): ...
    @staticmethod
    def get_formatted_principal(
        principal_name: str, host_name: str | None, realm: str
    ) -> str: ...
    def get_security_token_service_url(self, realm: str) -> str: ...
