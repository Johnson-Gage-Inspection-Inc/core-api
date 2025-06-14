from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.tenant.administration.internal.aad.permission_grant import (
    SPO3rdPartyAADPermissionGrantCollection as SPO3rdPartyAADPermissionGrantCollection,
)
from office365.sharepoint.tenant.administration.internal.appservice.permission_grant import (
    SPOWebAppServicePrincipalPermissionGrant as SPOWebAppServicePrincipalPermissionGrant,
)
from office365.sharepoint.tenant.administration.internal.appservice.permission_request import (
    SPOWebAppServicePrincipalPermissionRequest as SPOWebAppServicePrincipalPermissionRequest,
)

class SPOWebAppServicePrincipal(Entity):
    def __init__(self, context) -> None: ...
    def update_spfx_client_secret(self, secret_value): ...
    def update_spfx_third_party_app_id(self, app_id): ...
    @property
    def account_enabled(self) -> bool | None: ...
    @property
    def app_id(self) -> str | None: ...
    @property
    def reply_urls(self) -> StringCollection: ...
    @property
    def grant_manager(self): ...
    @property
    def permission_grants(self): ...
    @property
    def permission_requests(self): ...
    @property
    def entity_type_name(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
