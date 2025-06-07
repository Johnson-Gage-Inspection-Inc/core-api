from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.calendar.place import Place as Place
from office365.outlook.calendar.rooms.room import Room as Room
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class RoomList(Place):
    @property
    def email_address(self) -> str | None: ...
    @property
    def calendars(self) -> EntityCollection[Room]: ...
