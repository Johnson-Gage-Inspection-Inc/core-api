from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.publishing.pages.coauth_state import (
    SitePageCoAuthState as SitePageCoAuthState,
)
from office365.sharepoint.publishing.pages.dependency_metadata import (
    SitePageDependencyMetadata as SitePageDependencyMetadata,
)
from office365.sharepoint.publishing.pages.fields_data import (
    SitePageFieldsData as SitePageFieldsData,
)
from office365.sharepoint.publishing.pages.metadata import (
    SitePageMetadata as SitePageMetadata,
)
from office365.sharepoint.translation.status_collection import (
    TranslationStatusCollection as TranslationStatusCollection,
)

class SharePagePreviewByEmailFieldsData(ClientValue):
    message: Incomplete
    recipientEmails: Incomplete
    def __init__(
        self,
        message: Incomplete | None = None,
        recipient_emails: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...

class SitePage(SitePageMetadata):
    def checkout_page(self): ...
    def copy(self): ...
    def discard_page(self): ...
    def ensure_title_resource(self): ...
    def get_dependency_metadata(self): ...
    def get_version(self, version_id) -> None: ...
    def save_page(
        self,
        title,
        canvas_content: Incomplete | None = None,
        banner_image_url: Incomplete | None = None,
        topic_header: Incomplete | None = None,
    ): ...
    def save_draft(
        self,
        title,
        canvas_content: Incomplete | None = None,
        banner_image_url: Incomplete | None = None,
        topic_header: Incomplete | None = None,
    ): ...
    def save_page_as_draft(
        self,
        title,
        canvas_content: Incomplete | None = None,
        banner_image_url: Incomplete | None = None,
        topic_header: Incomplete | None = None,
    ): ...
    def save_page_as_template(self): ...
    def save_page_co_auth(self, page_stream): ...
    def demote_from_news(self): ...
    def promote_to_news(self): ...
    def publish(self): ...
    def schedule_publish(self, publish_start_date): ...
    def share_page_preview_by_email(self, message, recipient_emails): ...
    def start_co_auth(self): ...
    @property
    def canvas_content(self) -> str | None: ...
    @property
    def language(self) -> str | None: ...
    @canvas_content.setter
    def canvas_content(self, value: str) -> None: ...
    @property
    def layout_web_parts_content(self) -> str | None: ...
    @layout_web_parts_content.setter
    def layout_web_parts_content(self, value: str) -> None: ...
    @property
    def translations(self) -> TranslationStatusCollection: ...
    @property
    def entity_type_name(self) -> str: ...
