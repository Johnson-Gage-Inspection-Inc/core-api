from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.types.collections import GuidCollection as GuidCollection
from office365.sharepoint.navigation.menu_node import MenuNode as MenuNode

class MenuState(ClientValue):
    AudienceIds: Incomplete
    FriendlyUrlPrefix: Incomplete
    Nodes: Incomplete
    SimpleUrl: Incomplete
    SPSitePrefix: Incomplete
    def __init__(
        self,
        audience_ids: Incomplete | None = None,
        friendly_url_prefix: Incomplete | None = None,
        nodes: Incomplete | None = None,
        simple_url: Incomplete | None = None,
        site_prefix: Incomplete | None = None,
    ) -> None: ...
