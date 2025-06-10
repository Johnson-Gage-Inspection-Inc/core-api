from office365.entity import Entity as Entity
from office365.runtime.types.collections import StringCollection as StringCollection

class SingleValueLegacyExtendedProperty(Entity):
    @property
    def value(self) -> str | None: ...

class MultiValueLegacyExtendedProperty(Entity):
    @property
    def value(self): ...
