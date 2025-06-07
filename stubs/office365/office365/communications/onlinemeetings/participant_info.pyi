from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.runtime.client_value import ClientValue as ClientValue

class MeetingParticipantInfo(ClientValue):
    identity: Incomplete
    role: Incomplete
    upn: Incomplete
    def __init__(
        self,
        identity=...,
        role: Incomplete | None = None,
        upn: Incomplete | None = None,
    ) -> None: ...
