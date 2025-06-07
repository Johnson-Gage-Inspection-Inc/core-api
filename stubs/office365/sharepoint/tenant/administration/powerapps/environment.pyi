from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class PowerAppsEnvironment(ClientValue):
    AllocatedAICredits: Incomplete
    DisplayName: Incomplete
    IsDefault: Incomplete
    Name: Incomplete
    PurchasedAICredits: Incomplete
    def __init__(self, AllocatedAICredits: float = None, DisplayName: str = None, IsDefault: bool = None, Name: str = None, PurchasedAICredits: float = None) -> None: ...
    @property
    def entity_type_name(self) -> str: ...
