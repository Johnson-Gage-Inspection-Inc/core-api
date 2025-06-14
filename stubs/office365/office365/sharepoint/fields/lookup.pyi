from office365.sharepoint.fields.field import Field as Field

class FieldLookup(Field):
    @property
    def allow_multiple_values(self) -> bool | None: ...
    @allow_multiple_values.setter
    def allow_multiple_values(self, value: bool) -> None: ...
    @property
    def lookup_web_id(self) -> str | None: ...
    @lookup_web_id.setter
    def lookup_web_id(self, val: str) -> None: ...
    @property
    def lookup_list(self) -> str | None: ...
    @lookup_list.setter
    def lookup_list(self, val: str) -> None: ...
    @property
    def primary_field_id(self) -> str | None: ...
    @property
    def relationship_delete_behavior(self) -> int | None: ...
    @property
    def unlimited_length_in_document_library(self) -> bool | None: ...
