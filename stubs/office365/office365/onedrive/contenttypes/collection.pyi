from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.contenttypes.content_type import ContentType as ContentType
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class ContentTypeCollection(EntityCollection[ContentType]):
    def __init__(self, context, resource_path) -> None: ...
    def add(
        self,
        name,
        parent,
        description: Incomplete | None = None,
        group: Incomplete | None = None,
    ): ...
    def add_copy(self, content_type): ...
    def add_copy_from_content_type_hub(self, content_type_id): ...
    def get_compatible_hub_content_types(self): ...
