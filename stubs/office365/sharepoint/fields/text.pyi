from office365.sharepoint.fields.field import Field as Field

class FieldText(Field):
    @property
    def max_length(self): ...
    @max_length.setter
    def max_length(self, val) -> None: ...
