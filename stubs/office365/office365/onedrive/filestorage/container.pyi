from datetime import datetime

from _typeshed import Incomplete
from office365.entity import Entity as Entity

class FileStorageContainer(Entity):
    @property
    def created_datetime(self) -> datetime | None: ...
    @property
    def entity_type_name(self) -> str: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
