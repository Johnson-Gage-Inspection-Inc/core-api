from office365.azure_env import AzureEnvironment as AzureEnvironment
from office365.runtime.auth.authentication_context import (
    AuthenticationContext as AuthenticationContext,
)
from office365.runtime.auth.client_credential import (
    ClientCredential as ClientCredential,
)
from office365.runtime.auth.token_response import TokenResponse as TokenResponse
from office365.runtime.auth.user_credential import UserCredential as UserCredential
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.odata.request import ODataRequest as ODataRequest
from office365.runtime.odata.v3.json_light_format import (
    JsonLightFormat as JsonLightFormat,
)
from requests import Response
from typing import Callable
from typing_extensions import Self

class SharePointRequest(ODataRequest):
    def __init__(
        self,
        base_url,
        environment=...,
        allow_ntlm: bool = False,
        browser_mode: bool = False,
    ) -> None: ...
    def execute_request(self, path: str) -> Response: ...
    def with_credentials(
        self, credentials: UserCredential | ClientCredential
    ) -> Self: ...
    def with_client_certificate(
        self,
        tenant: str,
        client_id: str,
        thumbprint: str,
        cert_path: str | None = None,
        private_key: str | None = None,
        scopes: list[str] | None = None,
        passphrase: str | None = None,
    ) -> Self: ...
    def with_device_flow(
        self, tenant: str, client_id: str, scopes: list[str] | None = None
    ) -> Self: ...
    def with_interactive(
        self, tenant: str, client_id: str, scopes: list[str] | None = None
    ) -> Self: ...
    def with_access_token(self, token_func: Callable[[], TokenResponse]) -> Self: ...
    @property
    def authentication_context(self): ...
    @property
    def base_url(self): ...
    @property
    def service_root_url(self): ...
