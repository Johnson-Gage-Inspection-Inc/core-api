from _typeshed import Incomplete
from office365.communications.presences.status_message import (
    PresenceStatusMessage as PresenceStatusMessage,
)
from office365.entity import Entity as Entity
from office365.outlook.calendar.dateTimeTimeZone import (
    DateTimeTimeZone as DateTimeTimeZone,
)
from office365.outlook.mail.item_body import ItemBody as ItemBody
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class Presence(Entity):
    def clear_presence(self, session_id: Incomplete | None = None): ...
    def clear_user_preferred_presence(self): ...
    def set_presence(
        self,
        session_id,
        availability: Incomplete | None = None,
        activity: Incomplete | None = None,
        expiration_duration: Incomplete | None = None,
    ): ...
    def set_status_message(self, message, expiry: Incomplete | None = None): ...
    def set_user_preferred_presence(
        self,
        availability: str = "Available",
        activity: str = "Available",
        expiration_duration: Incomplete | None = None,
    ): ...
    @property
    def activity(self) -> str | None: ...
    @property
    def availability(self) -> str | None: ...
