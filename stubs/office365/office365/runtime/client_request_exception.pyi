from _typeshed import Incomplete
from requests import RequestException

class ClientRequestException(RequestException):
    payload: Incomplete
    args: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def code(self): ...
    @property
    def message_lang(self): ...
    @property
    def message(self) -> str: ...
