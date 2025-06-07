from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class GetListItemVersionsParameters(ClientValue):
    RowLimit: Incomplete
    SortDescending: Incomplete
    def __init__(
        self,
        row_limit: Incomplete | None = None,
        sort_descending: Incomplete | None = None,
    ) -> None: ...
