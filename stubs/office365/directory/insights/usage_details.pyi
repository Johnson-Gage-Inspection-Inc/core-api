from _typeshed import Incomplete
from datetime import datetime
from office365.runtime.client_value import ClientValue as ClientValue

class UsageDetails(ClientValue):
    lastAccessedDateTime: Incomplete
    lastModifiedDateTime: Incomplete
    def __init__(self, last_accessed_datetime: datetime | None = None, last_modified_datetime: datetime | None = None) -> None: ...
