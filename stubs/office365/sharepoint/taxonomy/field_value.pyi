from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class TaxonomyFieldValue(ClientValue):
    Label: Incomplete
    TermGuid: Incomplete
    WssId: Incomplete
    def __init__(self, label: Incomplete | None = None, term_guid: Incomplete | None = None, wss_id: int = -1) -> None: ...
    @property
    def entity_type_name(self): ...

class TaxonomyFieldValueCollection(ClientValueCollection[TaxonomyFieldValue]):
    def __init__(self, initial_values) -> None: ...
