from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.sitedesigns.metadata import (
    SiteDesignMetadata as SiteDesignMetadata,
)
from office365.sharepoint.sitedesigns.principal import (
    SiteDesignPrincipal as SiteDesignPrincipal,
)
from office365.sharepoint.sitedesigns.task import SiteDesignTask as SiteDesignTask
from office365.sharepoint.sitescripts.action_result import (
    SiteScriptActionResult as SiteScriptActionResult,
)
from office365.sharepoint.sitescripts.metadata import (
    SiteScriptMetadata as SiteScriptMetadata,
)
from office365.sharepoint.sitescripts.serialization_result import (
    SiteScriptSerializationResult as SiteScriptSerializationResult,
)

class SiteScriptUtility(Entity):
    def __init__(self, context) -> None: ...
    @staticmethod
    def create_list_design(context, info): ...
    @staticmethod
    def get_list_designs(context, store: Incomplete | None = None): ...
    @staticmethod
    def add_site_design_task(context, web_url, site_design_id): ...
    @staticmethod
    def get_site_script_from_list(
        context,
        list_url,
        options: Incomplete | None = None,
        return_type: Incomplete | None = None,
    ): ...
    @staticmethod
    def get_site_script_from_web(
        context,
        web_url,
        info: Incomplete | None = None,
        return_type: Incomplete | None = None,
    ): ...
    @staticmethod
    def create_site_script(context, title, description, content): ...
    @staticmethod
    def delete_site_script(context, _id): ...
    @staticmethod
    def get_site_scripts(context, store: Incomplete | None = None): ...
    @staticmethod
    def execute_site_script_action(context, action_definition): ...
    @staticmethod
    def create_site_design(context, info): ...
    @staticmethod
    def update_site_design(context, update_info): ...
    @staticmethod
    def get_site_designs(
        context, include_untargeted: bool = True, store: Incomplete | None = None
    ): ...
    @staticmethod
    def get_site_design_stages(context, site_design_id): ...
    @staticmethod
    def get_site_design_metadata(context, _id, store: Incomplete | None = None): ...
    @staticmethod
    def get_site_design_rights(context, id_): ...
    @staticmethod
    def grant_site_design_rights(context, _id, principal_names, granted_rights): ...
    @staticmethod
    def delete_site_design(context, _id): ...
    @property
    def entity_type_name(self): ...
