from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.runtime.client_value import ClientValue as ClientValue

class PublicationFacet(ClientValue):
    checkedOutBy: Incomplete
    level: Incomplete
    versionId: Incomplete
    def __init__(
        self,
        checked_out_by=...,
        level: Incomplete | None = None,
        version_id: Incomplete | None = None,
    ) -> None: ...
