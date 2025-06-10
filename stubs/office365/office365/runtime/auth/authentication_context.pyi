from _typeshed import Incomplete
from office365.azure_env import AzureEnvironment as AzureEnvironment
from office365.runtime.auth.client_credential import (
    ClientCredential as ClientCredential,
)
from office365.runtime.auth.providers.acs_token_provider import (
    ACSTokenProvider as ACSTokenProvider,
)
from office365.runtime.auth.providers.saml_token_provider import (
    SamlTokenProvider as SamlTokenProvider,
)
from office365.runtime.auth.token_response import TokenResponse as TokenResponse
from office365.runtime.auth.user_credential import UserCredential as UserCredential
from office365.runtime.compat import get_absolute_url as get_absolute_url
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from typing import Callable
from typing_extensions import Required, Self, TypedDict

class JSONToken(TypedDict):
    tokenType: Required[str]
    accessToken: Required[str]

class AuthenticationContext:
    url: Incomplete
    def __init__(
        self,
        url,
        environment: Incomplete | None = None,
        allow_ntlm: bool = False,
        browser_mode: bool = False,
    ) -> None: ...
    def with_client_certificate(
        self,
        tenant,
        client_id,
        thumbprint,
        cert_path: Incomplete | None = None,
        private_key: Incomplete | None = None,
        scopes: Incomplete | None = None,
        passphrase: Incomplete | None = None,
    ): ...
    def with_interactive(self, tenant, client_id, scopes: Incomplete | None = None): ...
    def with_device_flow(self, tenant, client_id, scopes: Incomplete | None = None): ...
    def with_access_token(self, token_func: Callable[[], JSONToken]) -> None: ...
    def with_credentials(
        self, credentials: UserCredential | ClientCredential
    ) -> AuthenticationContext: ...
    def acquire_token_for_user(self, username: str, password: str) -> Self: ...
    def acquire_token_for_app(self, client_id, client_secret): ...
    def authenticate_request(self, request: RequestOptions) -> None: ...
