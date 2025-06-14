from typing import Generic, Mapping, TypeVar

from _typeshed import Incomplete

T = TypeVar("T")

class ApiResponse(Generic[T]):
    status_code: Incomplete
    data: Incomplete
    headers: Incomplete
    raw_data: Incomplete
    def __init__(
        self,
        status_code: int,
        data: T | None = None,
        headers: Mapping[str, str] | None = None,
        raw_data: bytes | None = None,
    ) -> None: ...
