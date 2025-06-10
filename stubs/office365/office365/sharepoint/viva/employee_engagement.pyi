from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.viva.app_configuration import (
    AppConfiguration as AppConfiguration,
)
from office365.sharepoint.viva.connections_page import (
    VivaConnectionsPage as VivaConnectionsPage,
)
from office365.sharepoint.viva.dashboard_configuration import (
    DashboardConfiguration as DashboardConfiguration,
)
from office365.sharepoint.viva.home import VivaHome as VivaHome

class EmployeeEngagement(Entity):
    def __init__(self, context) -> None: ...
    def dashboard_content(self, override_language_code: Incomplete | None = None): ...
    def full_dashboard_content(
        self,
        canvas_as_json: Incomplete | None = None,
        include_personalization_data: Incomplete | None = None,
    ): ...
    def viva_home_configuration(self): ...
    def viva_home(self): ...
    @property
    def app_configuration(self): ...
    @property
    def viva_connections_page(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
