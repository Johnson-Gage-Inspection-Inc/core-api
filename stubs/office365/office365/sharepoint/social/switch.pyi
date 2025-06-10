from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class SPSocialSwitch(Entity):
    @staticmethod
    def is_following_feature_enabled(context): ...
    @property
    def entity_type_name(self): ...
