from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.runtime.client_value import ClientValue as ClientValue

class Shared(ClientValue):
    owner: Incomplete
    scope: Incomplete
    sharedBy: Incomplete
    sharedDateTime: Incomplete
    def __init__(
        self,
        owner=...,
        scope: Incomplete | None = None,
        shared_by=...,
        shared_datetime: Incomplete | None = None,
    ) -> None: ...
