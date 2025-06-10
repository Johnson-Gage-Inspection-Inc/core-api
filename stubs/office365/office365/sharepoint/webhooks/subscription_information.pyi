from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SubscriptionInformation(ClientValue):
    notificationUrl: Incomplete
    resource: Incomplete
    expirationDateTime: Incomplete
    clientState: Incomplete
    resourceData: Incomplete
    def __init__(
        self, notification_url, resource, expiration_datetime: Incomplete | None = None
    ) -> None: ...
    @property
    def entity_type_name(self): ...
