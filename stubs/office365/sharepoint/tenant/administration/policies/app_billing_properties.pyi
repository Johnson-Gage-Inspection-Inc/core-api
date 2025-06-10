from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SPOAppBillingProperties(ClientValue):
    ApplicationId: Incomplete
    AzureRegion: Incomplete
    IsActivated: Incomplete
    def __init__(
        self,
        application_id: Incomplete | None = None,
        azure_region: Incomplete | None = None,
        is_activated: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
