from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)
from office365.subscriptions.subscription import Subscription as Subscription

class SubscriptionCollection(EntityCollection[Subscription]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(
        self,
        change_type,
        notification_url,
        resource_path,
        expiration,
        client_state: Incomplete | None = None,
        latest_supported_tls_version: Incomplete | None = None,
        include_resource_data: Incomplete | None = None,
        encryption_certificate: Incomplete | None = None,
        encryption_certificate_id: Incomplete | None = None,
    ): ...
