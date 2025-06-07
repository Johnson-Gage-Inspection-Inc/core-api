from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class TextColumn(ClientValue):
    maxLength: Incomplete
    allowMultipleLines: Incomplete
    textType: Incomplete
    def __init__(self, max_length: Incomplete | None = None, allow_multiple_lines: Incomplete | None = None, text_type: Incomplete | None = None) -> None: ...
