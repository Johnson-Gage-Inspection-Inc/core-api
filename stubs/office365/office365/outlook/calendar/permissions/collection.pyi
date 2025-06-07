from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.calendar.email_address import EmailAddress as EmailAddress
from office365.outlook.calendar.permissions.permission import (
    CalendarPermission as CalendarPermission,
)

class CalendarPermissionCollection(EntityCollection[CalendarPermission]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, email_address, role): ...
