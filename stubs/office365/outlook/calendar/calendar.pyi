from _typeshed import Incomplete
from office365.directory.extensions.extended_property import (
    MultiValueLegacyExtendedProperty as MultiValueLegacyExtendedProperty,
)
from office365.directory.extensions.extended_property import (
    SingleValueLegacyExtendedProperty as SingleValueLegacyExtendedProperty,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.calendar.dateTimeTimeZone import (
    DateTimeTimeZone as DateTimeTimeZone,
)
from office365.outlook.calendar.email_address import EmailAddress as EmailAddress
from office365.outlook.calendar.events.collection import (
    EventCollection as EventCollection,
)
from office365.outlook.calendar.permissions.collection import (
    CalendarPermissionCollection as CalendarPermissionCollection,
)
from office365.outlook.calendar.schedule.information import (
    ScheduleInformation as ScheduleInformation,
)
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection

class Calendar(Entity):
    def allowed_calendar_sharing_roles(self, user): ...
    def get_schedule(
        self, schedules, start_time, end_time, availability_view_interval: int = 30
    ): ...
    @property
    def allowed_online_meeting_providers(self): ...
    @property
    def can_edit(self) -> bool | None: ...
    @property
    def can_share(self) -> bool | None: ...
    @property
    def can_view_private_items(self) -> bool | None: ...
    @property
    def change_key(self) -> str | None: ...
    @property
    def color(self) -> str | None: ...
    @property
    def default_online_meeting_provider(self) -> str | None: ...
    @property
    def name(self) -> str | None: ...
    @property
    def is_default_calendar(self) -> bool | None: ...
    @property
    def is_removable(self) -> bool | None: ...
    @property
    def is_tallying_responses(self) -> bool | None: ...
    @property
    def owner(self): ...
    @property
    def events(self) -> EventCollection: ...
    @property
    def calendar_view(self) -> EventCollection: ...
    @property
    def calendar_permissions(self): ...
    @property
    def multi_value_extended_properties(
        self,
    ) -> EntityCollection[MultiValueLegacyExtendedProperty]: ...
    @property
    def single_value_extended_properties(
        self,
    ) -> EntityCollection[SingleValueLegacyExtendedProperty]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
