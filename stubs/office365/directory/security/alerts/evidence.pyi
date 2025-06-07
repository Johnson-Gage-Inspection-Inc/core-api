from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class AlertEvidence(ClientValue):
    createdDateTime: Incomplete
    detailedRoles: Incomplete
    def __init__(self, created_datetime: Incomplete | None = None, detailed_roles: Incomplete | None = None) -> None: ...
