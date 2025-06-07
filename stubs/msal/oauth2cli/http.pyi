from _typeshed import Incomplete

class HttpClient:
    def post(self, url, params: Incomplete | None = None, data: Incomplete | None = None, headers: Incomplete | None = None, **kwargs): ...
    def get(self, url, params: Incomplete | None = None, headers: Incomplete | None = None, **kwargs): ...

class Response:
    status_code: int
    text: str
    headers: Incomplete
    def raise_for_status(self) -> None: ...
