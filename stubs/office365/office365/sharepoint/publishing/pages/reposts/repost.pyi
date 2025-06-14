from office365.sharepoint.publishing.pages.page import SitePage as SitePage

class RepostPage(SitePage):
    @property
    def is_banner_image_url_external(self) -> bool | None: ...
    @property
    def original_source_item_id(self) -> str | None: ...
    @property
    def original_source_url(self) -> str | None: ...
    @property
    def entity_type_name(self): ...
