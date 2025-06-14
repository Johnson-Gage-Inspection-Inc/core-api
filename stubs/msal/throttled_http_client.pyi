from .exceptions import MsalServiceError as MsalServiceError
from .oauth2cli.http import Response as Response
from _typeshed import Incomplete

DEVICE_AUTH_GRANT: str

class RetryAfterParser:
    FIELD_NAME_LOWER: Incomplete
    def __init__(self, default_value: Incomplete | None = None) -> None: ...
    def parse(self, *, result, **ignored): ...

class NormalizedResponse(Response):
    status_code: Incomplete
    text: Incomplete
    headers: Incomplete
    def __init__(self, raw_response) -> None: ...
    def raise_for_status(self) -> None: ...

class ThrottledHttpClientBase:
    http_client: Incomplete
    def __init__(
        self, http_client, *, http_cache: Incomplete | None = None
    ) -> None: ...
    def post(self, *args, **kwargs): ...
    def get(self, *args, **kwargs): ...
    def close(self): ...

class ThrottledHttpClient(ThrottledHttpClientBase):
    post: Incomplete
    get: Incomplete
    def __init__(
        self, *args, default_throttle_time: Incomplete | None = None, **kwargs
    ) -> None: ...
