from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.sitepages.base import BaseSitePage as BaseSitePage
from office365.onedrive.sitepages.canvas_layout import CanvasLayout as CanvasLayout
from office365.onedrive.sitepages.title_area import TitleArea as TitleArea
from office365.onedrive.sitepages.webparts.web_part import WebPart as WebPart
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class SitePage(BaseSitePage):
    def get_web_parts_by_position(
        self,
        web_part_index: Incomplete | None = None,
        horizontal_section_id: Incomplete | None = None,
        is_in_vertical_section: Incomplete | None = None,
        column_id: Incomplete | None = None,
    ): ...
    def checkin(self): ...
    def publish(self): ...
    @property
    def promotion_kind(self) -> str | None: ...
    @property
    def show_comments(self) -> bool | None: ...
    @property
    def show_recommended_pages(self) -> bool | None: ...
    @property
    def thumbnail_web_url(self) -> str | None: ...
    @property
    def title_area(self) -> str | None: ...
    @property
    def canvas_layout(self) -> CanvasLayout: ...
    @property
    def web_parts(self) -> EntityCollection[WebPart]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
