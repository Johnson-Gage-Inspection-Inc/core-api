from _typeshed import Incomplete
from office365.directory.security.alerts.alert import Alert as Alert
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.http.request_options import RequestOptions as RequestOptions

class AlertCollection(EntityCollection[Alert]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, title, description: Incomplete | None = None, severity: Incomplete | None = None, category: Incomplete | None = None, status: Incomplete | None = None, source: Incomplete | None = None, vendor_information: Incomplete | None = None): ...
