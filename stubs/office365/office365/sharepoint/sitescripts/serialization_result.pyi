from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class SiteScriptSerializationResult(ClientValue):
    JSON: Incomplete
    Warnings: Incomplete
    def __init__(
        self, json: Incomplete | None = None, warnings: Incomplete | None = None
    ) -> None: ...
