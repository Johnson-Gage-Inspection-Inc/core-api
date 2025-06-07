from office365.sharepoint.fields.field import Field as Field

class FieldComputed(Field):
    @property
    def enable_lookup(self) -> bool | None: ...
