from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.sharing.direct_abilities import DirectSharingAbilities as DirectSharingAbilities
from office365.sharepoint.sharing.link_abilities import SharingLinkAbilities as SharingLinkAbilities

class SharingAbilities(ClientValue):
    anonymousLinkAbilities: Incomplete
    anyoneLinkAbilities: Incomplete
    directSharingAbilities: Incomplete
    organizationLinkAbilities: Incomplete
    peopleSharingLinkAbilities: Incomplete
    def __init__(self, anonymous_link_abilities=..., anyone_link_abilities=..., direct_sharing_abilities=..., organization_link_abilities=..., people_sharing_link_abilities=...) -> None: ...
    @property
    def entity_type_name(self): ...
