from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.teams.apps.user_scope_installation import (
    UserScopeTeamsAppInstallation as UserScopeTeamsAppInstallation,
)
from office365.teams.associated_info import AssociatedTeamInfo as AssociatedTeamInfo

class UserTeamwork(Entity):
    @property
    def locale(self) -> str | None: ...
    @property
    def region(self) -> str | None: ...
    @property
    def associated_teams(self) -> EntityCollection[AssociatedTeamInfo]: ...
    @property
    def installed_apps(self) -> EntityCollection[UserScopeTeamsAppInstallation]: ...
    def send_activity_notification(
        self,
        topic,
        activity_type,
        chain_id,
        preview_text,
        template_parameters: Incomplete | None = None,
    ): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
