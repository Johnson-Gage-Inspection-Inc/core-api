from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ItemBody(ClientValue):
    content: Incomplete
    contentType: Incomplete
    def __init__(
        self, content: Incomplete | None = None, content_type: str = "Text"
    ) -> None: ...
    @staticmethod
    def text(content: str) -> ItemBody: ...
    @staticmethod
    def html(content: str) -> ItemBody: ...
