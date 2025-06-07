from _typeshed import Incomplete
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity

class AppPrincipalCredential(Entity):
    @staticmethod
    def create_from_symmetric_key(context, symmetric_key, not_before, not_after: Incomplete | None = None): ...
    @staticmethod
    def create_from_key_group(context, key_group_identifier): ...
