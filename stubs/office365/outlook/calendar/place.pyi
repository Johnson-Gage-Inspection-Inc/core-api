from office365.entity import Entity as Entity
from office365.outlook.mail.physical_address import PhysicalAddress as PhysicalAddress

class Place(Entity):
    @property
    def display_name(self) -> str | None: ...
    @property
    def address(self): ...
    @property
    def phone(self) -> str | None: ...
