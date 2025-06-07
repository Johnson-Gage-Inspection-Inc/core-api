from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class TaxonomyMetadata(ClientValue):
    anchorId: Incomplete
    def __init__(self, anchor_id: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
