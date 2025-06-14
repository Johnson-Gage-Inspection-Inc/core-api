from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.navigation.home_site_navigation_settings import (
    HomeSiteNavigationSettings as HomeSiteNavigationSettings,
)
from office365.sharepoint.navigation.menu_state import MenuState as MenuState
from office365.sharepoint.navigation.provider_type import (
    NavigationProviderType as NavigationProviderType,
)

class NavigationService(Entity):
    def __init__(self, context) -> None: ...
    def get_publishing_navigation_provider_type(self, map_provider_name=...): ...
    def global_nav(self): ...
    def global_nav_enabled(self): ...
    def set_global_nav_enabled(self, is_enabled): ...
    def menu_node_key(
        self, current_url, map_provider_name: Incomplete | None = None
    ): ...
    def menu_state(
        self,
        menu_node_key,
        map_provider_name,
        depth: Incomplete | None = None,
        custom_properties: Incomplete | None = None,
    ): ...
    def save_menu_state(self, menu_node_key, map_provider_name): ...
    @property
    def home_site_settings(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
    @property
    def entity_type_name(self): ...
