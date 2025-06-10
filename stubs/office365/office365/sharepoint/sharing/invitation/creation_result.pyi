from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SPInvitationCreationResult(ClientValue):
    Email: Incomplete
    InvitationLink: Incomplete
    Succeeded: Incomplete
    def __init__(self) -> None: ...
    @property
    def entity_type_name(self): ...
