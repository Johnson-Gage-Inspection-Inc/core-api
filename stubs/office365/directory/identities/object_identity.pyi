from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ObjectIdentity(ClientValue):
    signInType: Incomplete
    issuer: Incomplete
    issuerAssignedId: Incomplete
    def __init__(self, sign_in_type: Incomplete | None = None, issuer: Incomplete | None = None, issuer_assigned_id: Incomplete | None = None) -> None: ...
