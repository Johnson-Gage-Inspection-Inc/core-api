from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.fields.field import Field as Field

class FieldMultiChoice(Field):
    @property
    def fill_in_choice(self) -> bool | None: ...
    @property
    def mappings(self) -> str | None: ...
    @property
    def choices(self): ...
