from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.sharing.ability_status import SharingAbilityStatus as SharingAbilityStatus

class DirectSharingAbilities(ClientValue):
    canAddExternalPrincipal: Incomplete
    canAddInternalPrincipal: Incomplete
    canRequestGrantAccess: Incomplete
    supportsReviewPermission: Incomplete
    def __init__(self, can_add_external_principal=..., can_add_internal_principal=..., can_request_grant_access=..., supports_review_permission=...) -> None: ...
    @property
    def entity_type_name(self): ...
