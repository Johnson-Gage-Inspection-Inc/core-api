from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class Reputation(Entity):
    @staticmethod
    def set_rating(
        context, list_id, item_id, rating, return_type: Incomplete | None = None
    ): ...
    @staticmethod
    def set_like(
        context, list_id, item_id, like, return_type: Incomplete | None = None
    ): ...
    @property
    def entity_type_name(self): ...
