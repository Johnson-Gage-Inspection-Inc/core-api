from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.filestorage.container import (
    FileStorageContainer as FileStorageContainer,
)
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)

class FileStorageContainerCollection(EntityCollection[FileStorageContainer]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, display_name, container_type_id=...): ...
