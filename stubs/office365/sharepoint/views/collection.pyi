from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.lists.list import List as List
from office365.sharepoint.views.view import View as View

class ViewCollection(EntityCollection):
    def __init__(
        self,
        context: ClientContext,
        resource_path: ResourcePath | None = None,
        parent_list: List | None = None,
    ) -> None: ...
    def add(self, view_creation_information): ...
    def get_by_title(self, view_title): ...
    def get_by_id(self, view_id): ...
    @property
    def parent_list(self) -> List: ...
