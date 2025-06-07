from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class FileSystemInfo(ClientValue):
    createdDateTime: Incomplete
    lastAccessedDateTime: Incomplete
    lastModifiedDateTime: Incomplete
    def __init__(self, created_datetime: Incomplete | None = None, last_accessed_datetime: Incomplete | None = None, last_modified_datetime: Incomplete | None = None) -> None: ...
