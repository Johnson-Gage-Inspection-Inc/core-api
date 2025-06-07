from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class ActivityLogger(Entity):
    def log_activity(
        self,
        operation,
        list_id,
        list_item_unique_id,
        affected_resource_url,
        item_type,
        audit_creation_time,
        is_offline,
    ): ...
    @property
    def entity_type_name(self): ...
