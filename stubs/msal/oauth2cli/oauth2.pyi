from _typeshed import Incomplete

string_types: Incomplete

class BrowserInteractionTimeoutError(RuntimeError): ...

class BaseClient:
    @staticmethod
    def encode_saml_assertion(assertion): ...
    CLIENT_ASSERTION_TYPE_JWT: str
    CLIENT_ASSERTION_TYPE_SAML2: str
    client_assertion_encoders: Incomplete
    @property
    def session(self): ...
    @session.setter
    def session(self, value) -> None: ...
    configuration: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    client_assertion: Incomplete
    default_headers: Incomplete
    default_body: Incomplete
    logger: Incomplete
    def __init__(
        self,
        server_configuration: dict,
        client_id: str,
        http_client: Incomplete | None = None,
        client_secret: Optional[str] = None,
        client_assertion: Union[bytes, callable, None] = None,
        client_assertion_type: Optional[str] = None,
        default_headers: Optional[dict] = None,
        default_body: Optional[dict] = None,
        verify: Union[str, True, False, None] = None,
        proxies: Optional[dict] = None,
        timeout: Union[tuple, float, None] = None,
    ) -> None: ...
    def obtain_token_by_refresh_token(
        self, refresh_token, scope: Incomplete | None = None, **kwargs
    ): ...

class Client(BaseClient):
    DEVICE_FLOW: Incomplete
    DEVICE_FLOW_RETRIABLE_ERRORS: Incomplete
    GRANT_TYPE_SAML2: str
    GRANT_TYPE_JWT: str
    grant_assertion_encoders: Incomplete
    def initiate_device_flow(self, scope: list = None, **kwargs: dict) -> dict: ...
    def obtain_token_by_device_flow(self, flow, exit_condition=..., **kwargs): ...
    def build_auth_request_uri(
        self,
        response_type,
        redirect_uri: Incomplete | None = None,
        scope: Incomplete | None = None,
        state: Incomplete | None = None,
        **kwargs,
    ): ...
    def initiate_auth_code_flow(
        self,
        scope: Incomplete | None = None,
        redirect_uri: Incomplete | None = None,
        state: Incomplete | None = None,
        **kwargs,
    ): ...
    def obtain_token_by_auth_code_flow(
        self, auth_code_flow, auth_response, scope: Incomplete | None = None, **kwargs
    ): ...
    def obtain_token_by_browser(
        self,
        redirect_uri: Incomplete | None = None,
        auth_code_receiver: Incomplete | None = None,
        **kwargs,
    ): ...
    @staticmethod
    def parse_auth_response(params, state: Incomplete | None = None): ...
    def obtain_token_by_authorization_code(
        self,
        code,
        redirect_uri: Incomplete | None = None,
        scope: Incomplete | None = None,
        **kwargs,
    ): ...
    def obtain_token_by_username_password(
        self, username, password, scope: Incomplete | None = None, **kwargs
    ): ...
    def obtain_token_for_client(self, scope: Incomplete | None = None, **kwargs): ...
    on_obtaining_tokens: Incomplete
    on_removing_rt: Incomplete
    on_updating_rt: Incomplete
    def __init__(
        self,
        server_configuration,
        client_id,
        on_obtaining_tokens=...,
        on_removing_rt=...,
        on_updating_rt=...,
        **kwargs,
    ) -> None: ...
    def obtain_token_by_refresh_token(
        self,
        token_item,
        scope: Incomplete | None = None,
        rt_getter=...,
        on_removing_rt: Incomplete | None = None,
        on_updating_rt: Incomplete | None = None,
        **kwargs,
    ): ...
    def obtain_token_by_assertion(
        self, assertion, grant_type, scope: Incomplete | None = None, **kwargs
    ): ...
