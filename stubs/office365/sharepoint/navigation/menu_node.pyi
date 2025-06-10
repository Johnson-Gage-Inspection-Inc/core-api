from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.translation.resource_entry import (
    SPResourceEntry as SPResourceEntry,
)

class MenuNode(ClientValue):
    AudienceIds: Incomplete
    CurrentLCID: Incomplete
    IsDeleted: Incomplete
    IsHidden: Incomplete
    Key: Incomplete
    Nodes: Incomplete
    NodeType: Incomplete
    OpenInNewWindow: Incomplete
    SimpleUrl: Incomplete
    Title: Incomplete
    Translations: Incomplete
    def __init__(
        self,
        audience_ids: Incomplete | None = None,
        current_lcid: Incomplete | None = None,
        title: Incomplete | None = None,
        is_deleted: Incomplete | None = None,
        is_hidden: Incomplete | None = None,
        key: Incomplete | None = None,
        nodes: Incomplete | None = None,
        node_type: Incomplete | None = None,
        open_in_new_window: Incomplete | None = None,
        simple_url: Incomplete | None = None,
        translations: Incomplete | None = None,
    ) -> None: ...
