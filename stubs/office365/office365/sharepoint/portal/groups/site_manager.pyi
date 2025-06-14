from _typeshed import Incomplete
from office365.runtime.client_object import ClientObject as ClientObject
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.portal.channels.info_collection import (
    ChannelInfoCollection as ChannelInfoCollection,
)
from office365.sharepoint.portal.groups.creation_context import (
    GroupCreationContext as GroupCreationContext,
)
from office365.sharepoint.portal.groups.creation_information import (
    GroupCreationInformation as GroupCreationInformation,
)
from office365.sharepoint.portal.groups.site_info import GroupSiteInfo as GroupSiteInfo
from office365.sharepoint.portal.teams.recent_and_joined_response import (
    RecentAndJoinedTeamsResponse as RecentAndJoinedTeamsResponse,
)

class GroupSiteManager(ClientObject):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def can_user_create_group(self): ...
    def create_group_for_site(
        self,
        display_name,
        alias,
        is_public: Incomplete | None = None,
        optional_params: Incomplete | None = None,
    ): ...
    def create_group_ex(
        self, display_name, alias, is_public, optional_params: Incomplete | None = None
    ): ...
    def delete(self, site_url): ...
    def ensure_team_for_group(self): ...
    def get_group_creation_context(self): ...
    def get_status(self, group_id: str) -> ClientResult[GroupSiteInfo]: ...
    def get_current_user_joined_teams(
        self, get_logo_data: bool = False, force_cache_update: bool = False
    ): ...
    def get_current_user_shared_channel_member_groups(self): ...
    def get_team_channels(self, team_id, use_staging_endpoint: bool = False): ...
    def get_team_channels_direct(self, team_id): ...
    def get_team_channels_with_site_url(self, site_url): ...
    def notebook(self, group_id): ...
    def recent_and_joined_teams(
        self,
        include_recent: Incomplete | None = None,
        include_teams: Incomplete | None = None,
        include_pinned: Incomplete | None = None,
        existing_joined_teams_data: Incomplete | None = None,
    ): ...
    @property
    def entity_type_name(self): ...
