from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class FileCreationInformation(ClientValue):
    Url: Incomplete
    Overwrite: Incomplete
    Content: Incomplete
    XorHash: Incomplete
    def __init__(
        self,
        url: Incomplete | None = None,
        overwrite: bool = False,
        content: Incomplete | None = None,
    ) -> None: ...
    def to_json(self, json_format: Incomplete | None = None): ...
    @property
    def entity_type_name(self) -> None: ...
