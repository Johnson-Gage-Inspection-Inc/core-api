from _typeshed import Incomplete
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.contenttypes.content_type import ContentType as ContentType
from office365.sharepoint.contenttypes.entity_data import (
    ContentTypeEntityData as ContentTypeEntityData,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection

class ContentTypeCollection(EntityCollection[ContentType]):
    def __init__(
        self,
        context,
        resource_path: Incomplete | None = None,
        parent: Incomplete | None = None,
    ) -> None: ...
    def get_by_name(self, name): ...
    def get_by_id(self, content_type_id): ...
    def add(self, content_type_info): ...
    def create(
        self,
        name,
        description: Incomplete | None = None,
        group: Incomplete | None = None,
        parent_content_type: Incomplete | None = None,
    ): ...
    def add_available_content_type(self, content_type_id): ...
