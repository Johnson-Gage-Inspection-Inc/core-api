from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class AppPrincipalIdentityProvider(Entity):
    @staticmethod
    def external(context): ...
