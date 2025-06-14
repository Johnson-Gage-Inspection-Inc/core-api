from _typeshed import Incomplete
from office365.entity import Entity as Entity

class DeviceEnrollmentConfiguration(Entity):
    @property
    def created_datetime(self): ...
    @property
    def display_name(self) -> str | None: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
