from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SiteStateProperties(ClientValue):
    GroupSiteRelationship: Incomplete
    IsArchived: Incomplete
    IsSiteOnHold: Incomplete
    LockState: Incomplete
    def __init__(
        self,
        GroupSiteRelationship: int = None,
        IsArchived: bool = None,
        IsSiteOnHold: bool = None,
        LockState: int = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
