from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.alerts.alert import Alert as Alert
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection

class AlertCollection(EntityCollection[Alert]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, parameters): ...
    def contains(self, id_alert: str) -> ClientResult[bool]: ...
    def delete_alert_at_index(self, index): ...
    def get_by_id(self, id_alert): ...
