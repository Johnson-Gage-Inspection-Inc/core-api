from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity

class ThemeInfo(Entity):
    def get_theme_font_by_name(self, name, lcid): ...
    @property
    def accessible_description(self) -> str | None: ...
    @property
    def theme_background_image_uri(self) -> str | None: ...
