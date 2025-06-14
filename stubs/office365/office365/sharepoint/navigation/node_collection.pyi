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
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.navigation.node import NavigationNode as NavigationNode
from office365.sharepoint.navigation.node_creation_information import (
    NavigationNodeCreationInformation as NavigationNodeCreationInformation,
)

class NavigationNodeCollection(EntityCollection[NavigationNode]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(
        self, create_node_info: NavigationNodeCreationInformation
    ) -> NavigationNode: ...
    def move_after(self, node_id, previous_node_id): ...
    def get_by_index(self, index): ...
    def get_by_id(self, node_id): ...
