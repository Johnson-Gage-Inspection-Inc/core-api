from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class SharedWithMeItemCollection(Entity):
    @staticmethod
    def get_shared_with_me_external_items(context, top): ...
    @staticmethod
    def get_shared_with_me_items(
        context,
        top,
        skip_token: Incomplete | None = None,
        include_sharing_history: Incomplete | None = None,
    ): ...
