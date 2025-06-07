from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.portal.orglabels.context import OrgLabelsContext as OrgLabelsContext

class OrgLabelsContextList(ClientValue):
    IsLastPage: Incomplete
    Labels: Incomplete
    def __init__(self, is_last_page: Incomplete | None = None, labels: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
