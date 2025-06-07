from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class DriveRecipient(ClientValue):
    alias: Incomplete
    email: Incomplete
    objectId: Incomplete
    def __init__(self, alias: Incomplete | None = None, email: Incomplete | None = None, object_id: Incomplete | None = None) -> None: ...
    @staticmethod
    def from_email(value): ...
