from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class RecycleBinQueryInformation(ClientValue):
    IsAscending: Incomplete
    ItemState: Incomplete
    OrderBy: Incomplete
    PagingInfo: Incomplete
    RowLimit: Incomplete
    ShowOnlyMyItems: Incomplete
    def __init__(self, is_ascending, item_state, order_by, paging_info, row_limit, show_only_my_items) -> None: ...
