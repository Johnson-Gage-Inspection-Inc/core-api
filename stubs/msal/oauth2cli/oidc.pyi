from _typeshed import Incomplete

from . import oauth2 as oauth2

logger: Incomplete

def decode_part(raw, encoding: str = "utf-8"): ...

base64decode = decode_part

class IdTokenError(RuntimeError):
    def __init__(self, reason, now, claims) -> None: ...

class _IdTokenTimeError(IdTokenError):
    def __init__(self, reason, now, claims) -> None: ...
    def log(self) -> None: ...

class IdTokenIssuerError(IdTokenError): ...
class IdTokenAudienceError(IdTokenError): ...
class IdTokenNonceError(IdTokenError): ...

def decode_id_token(
    id_token,
    client_id: Incomplete | None = None,
    issuer: Incomplete | None = None,
    nonce: Incomplete | None = None,
    now: Incomplete | None = None,
): ...

class Prompt:
    NONE: str
    LOGIN: str
    CONSENT: str
    SELECT_ACCOUNT: str
    CREATE: str

class Client(oauth2.Client):
    def decode_id_token(self, id_token, nonce: Incomplete | None = None): ...
    def build_auth_request_uri(
        self, response_type, nonce: Incomplete | None = None, **kwargs
    ): ...
    def obtain_token_by_authorization_code(
        self, code, nonce: Incomplete | None = None, **kwargs
    ): ...
    def initiate_auth_code_flow(self, scope: Incomplete | None = None, **kwargs): ...
    def obtain_token_by_auth_code_flow(
        self, auth_code_flow, auth_response, **kwargs
    ): ...
    def obtain_token_by_browser(
        self,
        display: Incomplete | None = None,
        prompt: Incomplete | None = None,
        max_age: Incomplete | None = None,
        ui_locales: Incomplete | None = None,
        id_token_hint: Incomplete | None = None,
        login_hint: Incomplete | None = None,
        acr_values: Incomplete | None = None,
        **kwargs,
    ): ...
