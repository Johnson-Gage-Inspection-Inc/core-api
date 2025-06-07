from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class File(ClientValue):
    hashes: Incomplete
    mimeType: Incomplete
    processingMetadata: Incomplete
    def __init__(
        self, mime_type: Incomplete | None = None, hashes: Incomplete | None = None
    ) -> None: ...
