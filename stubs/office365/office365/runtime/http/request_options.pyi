from typing import Any

from _typeshed import Incomplete
from office365.runtime.http.http_method import HttpMethod as HttpMethod

class RequestOptions:
    url: Incomplete
    data: Incomplete
    headers: Incomplete
    auth: Incomplete
    method: Incomplete
    verify: bool
    stream: bool
    proxies: Incomplete
    def __init__(self, url, method=..., data: Incomplete | None = None) -> None: ...
    @property
    def is_file(self): ...
    @property
    def is_bytes(self): ...
    def set_header(self, name: str, value: Any) -> None: ...
    def ensure_header(self, name: str, value: Any) -> None: ...
