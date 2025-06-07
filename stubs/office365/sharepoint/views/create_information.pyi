from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class ViewCreationInformation(ClientValue):
    Title: Incomplete
    ViewTypeKind: Incomplete
    ViewFields: Incomplete
    ViewData: Incomplete
    RowLimit: Incomplete
    Query: Incomplete
    PersonalView: Incomplete
    Paged: Incomplete
    def __init__(self, title: Incomplete | None = None, view_type_kind: Incomplete | None = None, view_fields: Incomplete | None = None, view_data: Incomplete | None = None, row_limit: Incomplete | None = None, query: Incomplete | None = None, personal_view: Incomplete | None = None, paged: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
