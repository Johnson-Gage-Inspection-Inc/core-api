from _typeshed import Incomplete
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.sites.team_site_data import TeamSiteData as TeamSiteData
from office365.sharepoint.teams.channel import TeamChannel as TeamChannel

class TeamChannelManager(Entity):
    @staticmethod
    def add_team_channel(
        context,
        channel_url,
        private_channel: bool = False,
        private_channel_group_owner: Incomplete | None = None,
    ): ...
    @staticmethod
    def get_team_site_data(context, ignore_validation: bool = True): ...
    @staticmethod
    def save_conversations(
        context, list_url, list_item_id, updated_conversations_object
    ): ...
    @staticmethod
    def sync_teamsite_settings(context): ...
