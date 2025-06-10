from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.webs.time_zone_information import (
    TimeZoneInformation as TimeZoneInformation,
)

class TimeZone(Entity):
    def local_time_to_utc(self, date): ...
    def set_id(self, _id): ...
    @property
    def id(self): ...
    @property
    def description(self): ...
    @property
    def information(self): ...

class TimeZoneCollection(EntityCollection[TimeZone]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
