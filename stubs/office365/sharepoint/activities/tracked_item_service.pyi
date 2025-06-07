from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.activities.tracked_item_updates_request import TrackedItemUpdatesRequest as TrackedItemUpdatesRequest
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity import Entity as Entity

class TrackedItemService(Entity):
    @staticmethod
    def get_tracked_item_updates_for_user(context: ClientContext) -> ClientResult[str]: ...
    @property
    def entity_type_name(self): ...
