from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.category import OutlookCategory as OutlookCategory
from office365.outlook.locale_info import LocaleInfo as LocaleInfo
from office365.outlook.timezone_information import (
    TimeZoneInformation as TimeZoneInformation,
)
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

class OutlookUser(Entity):
    def supported_languages(self): ...
    def supported_time_zones(self): ...
    @property
    def master_categories(self) -> EntityCollection[OutlookCategory]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
