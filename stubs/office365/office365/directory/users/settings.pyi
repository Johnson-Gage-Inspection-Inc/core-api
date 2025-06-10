from _typeshed import Incomplete
from office365.directory.users.insights_settings import (
    UserInsightsSettings as UserInsightsSettings,
)
from office365.directory.users.storage import UserStorage as UserStorage
from office365.entity import Entity as Entity
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.schedule.shifts.preferences import (
    ShiftPreferences as ShiftPreferences,
)

class UserSettings(Entity):
    @property
    def contribution_to_content_discovery_as_organization_disabled(
        self,
    ) -> bool | None: ...
    @property
    def contribution_to_content_discovery_disabled(self) -> bool | None: ...
    @property
    def item_insights(self) -> UserInsightsSettings: ...
    @property
    def shift_preferences(self) -> ShiftPreferences: ...
    @property
    def storage(self) -> ShiftPreferences: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
