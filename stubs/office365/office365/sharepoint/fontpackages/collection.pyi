from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.fontpackages.font_package import FontPackage as FontPackage

class FontPackageCollection(EntityCollection):
    def __init__(
        self, context: ClientContext, resource_path: ResourcePath | None = None
    ) -> None: ...
    def get_by_title(self, title): ...
