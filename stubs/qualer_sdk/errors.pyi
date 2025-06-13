from _typeshed import Incomplete

__all__ = ["UnexpectedStatus"]

class UnexpectedStatus(Exception):
    status_code: Incomplete
    content: Incomplete
    def __init__(self, status_code: int, content: bytes) -> None: ...
