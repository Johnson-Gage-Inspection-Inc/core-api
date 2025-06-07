from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class PersonalWeb(Entity):
    @staticmethod
    def fix_permission_inheritance(context): ...
    @property
    def entity_type_name(self): ...
