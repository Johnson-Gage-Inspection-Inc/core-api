from _typeshed import Incomplete
from office365.runtime.client_object_collection import (
    ClientObjectCollection as ClientObjectCollection,
)
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.principal.users.user import User as User
from office365.sharepoint.tenant.administration.siteinfo_for_site_picker import (
    SiteInfoForSitePicker as SiteInfoForSitePicker,
)
from office365.sharepoint.tenant.administration.theme_properties import (
    ThemeProperties as ThemeProperties,
)
from office365.sharepoint.tenant.management.externalusers.results.get import (
    GetExternalUsersResults as GetExternalUsersResults,
)
from office365.sharepoint.tenant.management.externalusers.results.remove import (
    RemoveExternalUsersResults as RemoveExternalUsersResults,
)
from office365.sharepoint.tenant.management.externalusers.results.session_revocation import (
    SPOUserSessionRevocationResult as SPOUserSessionRevocationResult,
)
from typing_extensions import Self

class Office365Tenant(Entity):
    def __init__(self, context) -> None: ...
    @property
    def addressbar_link_permission(self) -> int | None: ...
    @property
    def allow_comments_text_on_email_enabled(self) -> bool | None: ...
    @property
    def allow_editing(self) -> bool | None: ...
    @property
    def ai_builder_site_info_list(self): ...
    def add_tenant_cdn_origin(self, cdn_type, origin_url): ...
    def disable_sharing_for_non_owners_of_site(self, site_url): ...
    def get_tenant_cdn_enabled(self, cdn_type): ...
    def set_block_download_file_type_policy_data(
        self,
        block_download_file_type_policy: bool,
        file_type_ids: list[int],
        excluded_block_download_group_ids: list[str],
    ) -> Self: ...
    def set_tenant_cdn_enabled(self, cdn_type, is_enabled): ...
    def remove_tenant_cdn_origin(self, cdn_type, origin_url): ...
    def get_tenant_cdn_policies(self, cdn_type): ...
    def set_tenant_cdn_policy(self, cdn_type, policy, policy_value): ...
    def revoke_all_user_sessions(self, user): ...
    def get_external_users(
        self,
        position: int = 0,
        page_size: int = 50,
        _filter: Incomplete | None = None,
        sort_order: int = 0,
    ): ...
    def remove_external_users(self, unique_ids: Incomplete | None = None): ...
    def get_all_tenant_themes(self): ...
    def add_tenant_theme(self, name, theme_json): ...
    def delete_tenant_theme(self, name): ...
    def queue_import_profile_properties(
        self, id_type, source_data_id_property, property_map, source_uri
    ): ...
