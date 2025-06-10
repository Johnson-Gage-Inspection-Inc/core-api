from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ImageFieldValue(ClientValue):
    serverRelativeUrl: Incomplete
    type: Incomplete
    fileName: Incomplete
    nativeFile: Incomplete
    fieldName: str
    serverUrl: Incomplete
    fieldId: Incomplete
    id: Incomplete
    def __init__(self, server_relative_url: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self) -> None: ...
