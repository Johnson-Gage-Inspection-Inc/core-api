from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.sites.home.reference import (
    SPHSiteReference as SPHSiteReference,
)

class SPHSite(Entity):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def details(self): ...
    @staticmethod
    def is_comm_site(context, site_url, return_value: Incomplete | None = None): ...
    @staticmethod
    def is_modern_site_with_horizontal_nav(
        context, site_url, return_type: Incomplete | None = None
    ): ...
    @staticmethod
    def is_valid_home_site(
        context, site_url, return_value: Incomplete | None = None
    ): ...
    @staticmethod
    def validate_home_site(context, site_url, validation_action_type): ...
    @staticmethod
    def set_as_home_site(
        context,
        site_url,
        viva_connections_default_start: Incomplete | None = None,
        return_value: Incomplete | None = None,
    ): ...
