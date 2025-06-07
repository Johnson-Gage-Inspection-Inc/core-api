from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SharePointIds(ClientValue):
    listId: Incomplete
    listItemId: Incomplete
    listItemUniqueId: Incomplete
    siteId: Incomplete
    siteUrl: Incomplete
    tenantId: Incomplete
    webId: Incomplete
    def __init__(self, list_id: Incomplete | None = None, list_item_id: Incomplete | None = None, list_item_unique_id: Incomplete | None = None, siteId: Incomplete | None = None, siteUrl: Incomplete | None = None, tenantId: Incomplete | None = None, webId: Incomplete | None = None) -> None: ...
