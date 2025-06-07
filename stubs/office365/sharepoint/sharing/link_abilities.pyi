from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.sharing.ability_status import SharingAbilityStatus as SharingAbilityStatus

class SharingLinkAbilities(ClientValue):
    canAddNewExternalPrincipals: Incomplete
    canDeleteEditLink: Incomplete
    canDeleteManageListLink: Incomplete
    canGetEditLink: Incomplete
    canGetReadLink: Incomplete
    def __init__(self, can_add_new_external_principals=..., can_delete_edit_link=..., can_delete_manage_list_link=..., can_get_edit_link=..., can_get_read_link=...) -> None: ...
    @property
    def entity_type_name(self): ...
