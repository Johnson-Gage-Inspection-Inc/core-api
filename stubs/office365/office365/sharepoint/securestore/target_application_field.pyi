from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class TargetApplicationField(Entity):
    @staticmethod
    def create(context, name, masked, credential_type): ...
    @property
    def entity_type_name(self): ...
