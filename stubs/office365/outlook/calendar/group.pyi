from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.calendar.calendar import Calendar as Calendar
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class CalendarGroup(Entity):
    @property
    def name(self) -> str | None: ...
    @property
    def class_id(self) -> str | None: ...
    @property
    def calendars(self) -> EntityCollection[Calendar]: ...
