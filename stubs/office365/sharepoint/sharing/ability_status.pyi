from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SharingAbilityStatus(ClientValue):
    disabledReason: Incomplete
    enabled: Incomplete
    def __init__(self, disabled_reason: Incomplete | None = None, enabled: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
