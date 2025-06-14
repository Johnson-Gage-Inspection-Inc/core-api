from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.administration.orgassets.org_assets import (
    OrgAssets as OrgAssets,
)
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.clientsidecomponent.query_result import (
    SPClientSideComponentQueryResult as SPClientSideComponentQueryResult,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.files.file import File as File
from office365.sharepoint.publishing.file_picker_options import (
    FilePickerOptions as FilePickerOptions,
)
from office365.sharepoint.publishing.pages.collection import (
    SitePageCollection as SitePageCollection,
)
from office365.sharepoint.publishing.pages.page import SitePage as SitePage
from office365.sharepoint.publishing.primary_city_time import (
    PrimaryCityTime as PrimaryCityTime,
)
from office365.sharepoint.publishing.sites.communication.site import (
    CommunicationSite as CommunicationSite,
)

class SitePageService(Entity):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    @property
    def pages(self) -> SitePageCollection: ...
    @property
    def communication_site(self) -> CommunicationSite: ...
    @property
    def entity_type_name(self): ...
    def create_page(self, title: str, language: str | None = None) -> SitePage: ...
    def create_and_publish_page(self, title): ...
    def can_create_page(self): ...
    def can_create_promoted_page(self): ...
    @staticmethod
    def get_current_user_memberships(
        context: ClientContext, scenario: str | None = None
    ) -> ClientResult[StringCollection]: ...
    @staticmethod
    def get_time_zone(context: ClientContext, city_name: str) -> PrimaryCityTime: ...
    @staticmethod
    def compute_file_name(context: ClientContext, title: str) -> ClientResult[str]: ...
    @staticmethod
    def get_available_full_page_applications(
        context,
        include_errors: Incomplete | None = None,
        project: Incomplete | None = None,
    ): ...
    @staticmethod
    def is_file_picker_external_image_search_enabled(
        context: ClientContext,
    ) -> ClientResult[bool]: ...
    @staticmethod
    def org_assets(context: ClientContext) -> ClientResult[OrgAssets]: ...
    @staticmethod
    def file_picker_tab_options(
        context: ClientContext,
    ) -> ClientResult[FilePickerOptions]: ...
    def add_image(self, page_name, image_file_name, image_stream): ...
    def add_image_from_external_url(
        self, page_name, image_file_name, external_url, sub_folder_name, page_id
    ): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
