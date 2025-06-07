from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.sharing.inherited_from import InheritedFrom as InheritedFrom
from office365.sharepoint.sharing.links.info import SharingLinkInfo as SharingLinkInfo
from office365.sharepoint.sharing.principal import Principal as Principal

class LinkInfo(ClientValue):
    inherited_from: Incomplete
    isInherited: Incomplete
    linkDetails: Incomplete
    linkMembers: Incomplete
    linkStatus: Incomplete
    totalLinkMembersCount: Incomplete
    def __init__(
        self,
        inherited_from=...,
        is_inherited: Incomplete | None = None,
        link_details=...,
        link_members: Incomplete | None = None,
        link_status: Incomplete | None = None,
        total_link_members_count: Incomplete | None = None,
    ) -> None: ...
