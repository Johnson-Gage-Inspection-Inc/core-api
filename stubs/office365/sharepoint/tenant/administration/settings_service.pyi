from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.tenant.administration.default_time_zone_id import (
    TenantDefaultTimeZoneId as TenantDefaultTimeZoneId,
)
from office365.sharepoint.tenant.administration.smtp_server import (
    SmtpServer as SmtpServer,
)
from office365.sharepoint.tenant.administration.types import (
    AutoQuotaEnabled as AutoQuotaEnabled,
)
from office365.sharepoint.tenant.administration.types import (
    DisableGroupify as DisableGroupify,
)
from office365.sharepoint.tenant.administration.types import (
    DisableSelfServiceSiteCreation as DisableSelfServiceSiteCreation,
)
from office365.sharepoint.tenant.administration.types import (
    EnableAutoNewsDigest as EnableAutoNewsDigest,
)

class TenantAdminSettingsService(Entity):
    def __init__(self, context) -> None: ...
    def get_tenant_sharing_status(self): ...
    @property
    def auto_quota_enabled(self): ...
    @property
    def available_managed_paths_for_site_creation(self): ...
    @property
    def disable_groupify(self): ...
    @property
    def disable_self_service_site_creation(self): ...
    @property
    def enable_auto_news_digest(self): ...
    @property
    def smtp_server(self): ...
    @property
    def tenant_default_time_zone_id(self): ...
    @property
    def entity_type_name(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
