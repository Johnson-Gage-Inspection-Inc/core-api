from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class PeoplePickerQuerySettings(ClientValue):
    ExcludeAllUsersOnTenantClaim: Incomplete
    IsSharing: Incomplete
    def __init__(self, exclude_all_users_on_tenant_claim: Incomplete | None = None, is_sharing: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
