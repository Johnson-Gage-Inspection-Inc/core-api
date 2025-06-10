from .wstrust_response import *
from .authority import Authority as Authority, WORLD_WIDE as WORLD_WIDE
from .oauth2cli import Client as Client, JwtAssertionCreator as JwtAssertionCreator
from .oauth2cli.oidc import decode_part as decode_part
from .sku import SKU as SKU, __version__ as __version__
from .throttled_http_client import ThrottledHttpClient as ThrottledHttpClient
from .token_cache import TokenCache as TokenCache
from _typeshed import Incomplete

logger: Incomplete

def extract_certs(public_cert_content): ...

class _ClientWithCcsRoutingInfo(Client):
    def initiate_auth_code_flow(self, **kwargs): ...
    def obtain_token_by_auth_code_flow(
        self, auth_code_flow, auth_response, **kwargs
    ): ...
    def obtain_token_by_username_password(self, username, password, **kwargs): ...

class ClientApplication:
    ACQUIRE_TOKEN_SILENT_ID: str
    ACQUIRE_TOKEN_BY_REFRESH_TOKEN: str
    ACQUIRE_TOKEN_BY_USERNAME_PASSWORD_ID: str
    ACQUIRE_TOKEN_ON_BEHALF_OF_ID: str
    ACQUIRE_TOKEN_BY_DEVICE_FLOW_ID: str
    ACQUIRE_TOKEN_FOR_CLIENT_ID: str
    ACQUIRE_TOKEN_BY_AUTHORIZATION_CODE_ID: str
    ACQUIRE_TOKEN_INTERACTIVE: str
    GET_ACCOUNTS_ID: str
    REMOVE_ACCOUNT_ID: str
    ATTEMPT_REGION_DISCOVERY: bool
    DISABLE_MSAL_FORCE_REGION: bool
    client_id: Incomplete
    client_credential: Incomplete
    client_claims: Incomplete
    http_client: Incomplete
    app_name: Incomplete
    app_version: Incomplete
    authority: Incomplete
    token_cache: Incomplete
    authority_groups: Incomplete
    def __init__(
        self,
        client_id,
        client_credential: Incomplete | None = None,
        authority: Incomplete | None = None,
        validate_authority: bool = True,
        token_cache: Incomplete | None = None,
        http_client: Incomplete | None = None,
        verify: bool = True,
        proxies: Incomplete | None = None,
        timeout: Incomplete | None = None,
        client_claims: Incomplete | None = None,
        app_name: Incomplete | None = None,
        app_version: Incomplete | None = None,
        client_capabilities: Incomplete | None = None,
        azure_region: Incomplete | None = None,
        exclude_scopes: Incomplete | None = None,
        http_cache: Incomplete | None = None,
        instance_discovery: Incomplete | None = None,
        allow_broker: Incomplete | None = None,
        enable_pii_log: Incomplete | None = None,
        oidc_authority: Incomplete | None = None,
    ) -> None: ...
    def is_pop_supported(self): ...
    def initiate_auth_code_flow(
        self,
        scopes: list[str],
        redirect_uri: Incomplete | None = None,
        state: Incomplete | None = None,
        prompt: Incomplete | None = None,
        login_hint: str | None = None,
        domain_hint: str | None = None,
        claims_challenge: Incomplete | None = None,
        max_age: Incomplete | None = None,
        response_mode: str | None = None,
    ): ...
    def get_authorization_request_url(
        self,
        scopes: list[str],
        login_hint: str | None = None,
        state: Incomplete | None = None,
        redirect_uri: Incomplete | None = None,
        response_type: str = "code",
        prompt: Incomplete | None = None,
        nonce: Incomplete | None = None,
        domain_hint: str | None = None,
        claims_challenge: Incomplete | None = None,
        **kwargs,
    ): ...
    def acquire_token_by_auth_code_flow(
        self, auth_code_flow, auth_response, scopes: Incomplete | None = None, **kwargs
    ): ...
    def acquire_token_by_authorization_code(
        self,
        code,
        scopes,
        redirect_uri: Incomplete | None = None,
        nonce: Incomplete | None = None,
        claims_challenge: Incomplete | None = None,
        **kwargs,
    ): ...
    def get_accounts(self, username: Incomplete | None = None): ...
    def remove_account(self, account) -> None: ...
    def acquire_token_silent(
        self,
        scopes: List[str],
        account: Account | None,
        authority: Incomplete | None = None,
        force_refresh: bool | None = False,
        claims_challenge: Incomplete | None = None,
        auth_scheme: Incomplete | None = None,
        **kwargs,
    ): ...
    def acquire_token_silent_with_error(
        self,
        scopes: List[str],
        account: Account | None,
        authority: Incomplete | None = None,
        force_refresh: bool | None = False,
        claims_challenge: Incomplete | None = None,
        auth_scheme: Incomplete | None = None,
        **kwargs,
    ): ...
    def acquire_token_by_refresh_token(self, refresh_token, scopes, **kwargs): ...
    def acquire_token_by_username_password(
        self,
        username,
        password,
        scopes,
        claims_challenge: Incomplete | None = None,
        auth_scheme: Incomplete | None = None,
        **kwargs,
    ): ...

class PublicClientApplication(ClientApplication):
    DEVICE_FLOW_CORRELATION_ID: str
    CONSOLE_WINDOW_HANDLE: Incomplete
    def __init__(
        self,
        client_id,
        client_credential: Incomplete | None = None,
        *,
        enable_broker_on_windows: Incomplete | None = None,
        enable_broker_on_mac: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def acquire_token_interactive(
        self,
        scopes: list[str],
        prompt: Incomplete | None = None,
        login_hint: str | None = None,
        domain_hint: str | None = None,
        claims_challenge: Incomplete | None = None,
        timeout: Incomplete | None = None,
        port: Incomplete | None = None,
        extra_scopes_to_consent: Incomplete | None = None,
        max_age: Incomplete | None = None,
        parent_window_handle: Incomplete | None = None,
        on_before_launching_ui: Incomplete | None = None,
        auth_scheme: Incomplete | None = None,
        **kwargs,
    ): ...
    def initiate_device_flow(self, scopes: Incomplete | None = None, **kwargs): ...
    def acquire_token_by_device_flow(
        self, flow, claims_challenge: Incomplete | None = None, **kwargs
    ): ...

class ConfidentialClientApplication(ClientApplication):
    def acquire_token_for_client(
        self, scopes, claims_challenge: Incomplete | None = None, **kwargs
    ) -> dict: ...
    def remove_tokens_for_client(self) -> None: ...
    def acquire_token_on_behalf_of(
        self,
        user_assertion,
        scopes,
        claims_challenge: Incomplete | None = None,
        **kwargs,
    ): ...
