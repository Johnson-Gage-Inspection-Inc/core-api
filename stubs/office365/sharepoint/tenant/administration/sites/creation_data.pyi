from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SiteCreationData(ClientValue):
    Count: Incomplete
    SiteCreationSourceGuid: Incomplete
    def __init__(
        self,
        count: Incomplete | None = None,
        site_creation_source_guid: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
