from _typeshed import Incomplete
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.webs.information import WebInformation as WebInformation

class WebInformationCollection(EntityCollection[WebInformation]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_by_id(self, _id): ...
