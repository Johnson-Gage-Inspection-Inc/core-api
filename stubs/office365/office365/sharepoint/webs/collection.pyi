from _typeshed import Incomplete
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.internal.paths.web import WebPath as WebPath
from office365.sharepoint.webs.web import Web as Web

class WebCollection(EntityCollection[Web]):
    def __init__(
        self,
        context,
        resource_path: Incomplete | None = None,
        parent_web: Incomplete | None = None,
    ) -> None: ...
    def add(self, web_creation_information): ...
    def create_typed_object(
        self,
        initial_properties: Incomplete | None = None,
        resource_path: Incomplete | None = None,
    ): ...
    @property
    def resource_url(self): ...
