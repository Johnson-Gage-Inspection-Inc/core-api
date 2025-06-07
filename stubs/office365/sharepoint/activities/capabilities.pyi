from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ActivityCapabilities(ClientValue):
    clientActivitiesEnabled: Incomplete
    clientActivitiesNotificationEnabled: Incomplete
    enabled: Incomplete
    def __init__(self, client_activities_enabled: Incomplete | None = None, client_activities_notification_enabled: Incomplete | None = None, enabled: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
