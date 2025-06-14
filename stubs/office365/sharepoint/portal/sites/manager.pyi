from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.portal.sites.creation_request import (
    SPSiteCreationRequest as SPSiteCreationRequest,
)
from office365.sharepoint.portal.sites.creation_response import (
    SPSiteCreationResponse as SPSiteCreationResponse,
)
from office365.sharepoint.teams.site_owner_response import (
    GetTeamChannelSiteOwnerResponse as GetTeamChannelSiteOwnerResponse,
)
from office365.sharepoint.viva.site_request_info import (
    VivaSiteRequestInfo as VivaSiteRequestInfo,
)

class SPSiteManager(Entity):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def create(self, title, site_url, owner: Incomplete | None = None): ...
    def delete(self, site_id): ...
    def get_status(self, site_url): ...
    def get_site_url(self, site_id): ...
    def get_team_channel_site_owner(self, site_id): ...
    def viva_backend_site_url_from_name(self, site_name): ...
