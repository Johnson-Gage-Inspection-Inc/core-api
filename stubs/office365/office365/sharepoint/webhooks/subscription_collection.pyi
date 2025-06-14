from _typeshed import Incomplete
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.webhooks.subscription import Subscription as Subscription
from office365.sharepoint.webhooks.subscription_information import (
    SubscriptionInformation as SubscriptionInformation,
)

class SubscriptionCollection(EntityCollection[Subscription]):
    def __init__(
        self,
        context,
        resource_path: Incomplete | None = None,
        parent: Incomplete | None = None,
    ) -> None: ...
    def get_by_id(self, _id): ...
    def add(self, parameters): ...
    def remove(self, subscription_id): ...
