from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.webparts.definition import (
    WebPartDefinition as WebPartDefinition,
)
from office365.sharepoint.webparts.definition_collection import (
    WebPartDefinitionCollection as WebPartDefinitionCollection,
)

class LimitedWebPartManager(Entity):
    def export_web_part(self, web_part: None) -> ClientResult[str]: ...
    def import_web_part(self, web_part_xml): ...
    @property
    def web_parts(self): ...
    @property
    def entity_type_name(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
