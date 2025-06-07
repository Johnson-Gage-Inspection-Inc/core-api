from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class FolderView(ClientValue):
    sortBy: Incomplete
    sortOrder: Incomplete
    viewType: Incomplete
    def __init__(
        self,
        sort_by: Incomplete | None = None,
        sort_order: Incomplete | None = None,
        view_type: Incomplete | None = None,
    ) -> None: ...
