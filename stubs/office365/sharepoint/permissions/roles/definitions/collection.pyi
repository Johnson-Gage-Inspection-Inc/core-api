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
from office365.sharepoint.permissions.roles.definitions.creation_information import (
    RoleDefinitionCreationInformation as RoleDefinitionCreationInformation,
)
from office365.sharepoint.permissions.roles.definitions.definition import (
    RoleDefinition as RoleDefinition,
)

class RoleDefinitionCollection(EntityCollection[RoleDefinition]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(
        self,
        base_permissions,
        name,
        description: Incomplete | None = None,
        order: Incomplete | None = None,
    ): ...
    def recreate_missing_default_role_definitions(self): ...
    def remove_all(self): ...
    def get_by_name(self, name): ...
    def get_by_id(self, _id): ...
    def get_by_type(self, role_type): ...
