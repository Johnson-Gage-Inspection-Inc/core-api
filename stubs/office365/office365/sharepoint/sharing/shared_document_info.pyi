from office365.sharepoint.contenttypes.content_type_id import (
    ContentTypeId as ContentTypeId,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.sharing.principal import Principal as Principal

class SharedDocumentInfo(Entity):
    @property
    def activity(self) -> str | None: ...
    @property
    def author(self): ...
    @property
    def caller_stack(self) -> str | None: ...
    @property
    def color_hex(self) -> str | None: ...
    @property
    def color_tag(self) -> str | None: ...
    @property
    def content_type_id(self) -> str | None: ...
    @property
    def entity_type_name(self): ...
