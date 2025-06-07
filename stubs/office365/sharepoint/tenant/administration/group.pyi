from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity

class GroupInfo(ClientValue):
    @property
    def entity_type_name(self): ...

class SPOGroup(Entity):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add_as_group_owner_and_member(self, group_id, user_id, user_principal_name): ...
    def get_group_info(self, group_id): ...
    @property
    def entity_type_name(self): ...
