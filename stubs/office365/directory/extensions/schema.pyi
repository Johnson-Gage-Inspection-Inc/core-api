from office365.entity import Entity as Entity
from office365.runtime.types.collections import StringCollection as StringCollection

class SchemaExtension(Entity):
    @property
    def target_types(self): ...
