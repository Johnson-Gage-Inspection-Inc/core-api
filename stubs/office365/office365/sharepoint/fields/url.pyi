from office365.sharepoint.fields.field import Field as Field

class FieldUrl(Field):
    @property
    def display_format(self) -> int | None: ...
