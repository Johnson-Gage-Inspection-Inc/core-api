from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.portal.userprofiles.sharedwithme.document import (
    SharedWithMeDocument as SharedWithMeDocument,
)

class SharedWithMeItems(Entity):
    @staticmethod
    def shared_with_me(context): ...
    @property
    def entity_type_name(self): ...
