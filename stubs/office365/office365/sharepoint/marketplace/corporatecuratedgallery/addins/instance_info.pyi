from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SPAddinInstanceInfo(ClientValue):
    appIdentifier: Incomplete
    appInstanceId: Incomplete
    tenantAppData: Incomplete
    tenantAppDataUpdateTime: Incomplete
    title: Incomplete
    def __init__(
        self,
        app_identifier: Incomplete | None = None,
        app_instance_id: Incomplete | None = None,
        tenant_app_data: Incomplete | None = None,
        tenant_app_data_update_time: Incomplete | None = None,
        title: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
