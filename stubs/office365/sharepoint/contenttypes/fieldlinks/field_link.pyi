from office365.sharepoint.entity import Entity as Entity

class FieldLink(Entity):
    @property
    def id(self) -> str | None: ...
    @property
    def field_internal_name(self) -> str | None: ...
    @property
    def read_only(self) -> bool | None: ...
    @property
    def hidden(self) -> bool | None: ...
    @property
    def required(self) -> bool | None: ...
    @property
    def show_in_display_form(self) -> bool | None: ...
