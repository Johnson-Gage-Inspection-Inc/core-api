from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.activities.facets.revision_set import RevisionSetFacet as RevisionSetFacet

class ActivityClientRequest(ClientValue):
    revisionSet: Incomplete
    def __init__(self, revisionSet=...) -> None: ...
    @property
    def entity_type_name(self): ...
