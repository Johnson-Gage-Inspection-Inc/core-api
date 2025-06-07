from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
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
from office365.sharepoint.principal.groups.creation_information import (
    GroupCreationInformation as GroupCreationInformation,
)
from office365.sharepoint.principal.groups.group import Group as Group
from office365.sharepoint.utilities.principal_info import PrincipalInfo as PrincipalInfo

class GroupCollection(EntityCollection[Group]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def expand_to_principals(self, max_count): ...
    def add(self, title, description: Incomplete | None = None): ...
    def get_by_id(self, group_id): ...
    def get_by_name(self, group_name): ...
    def remove_by_id(self, group_id): ...
    def remove_by_login_name(self, group_name): ...
