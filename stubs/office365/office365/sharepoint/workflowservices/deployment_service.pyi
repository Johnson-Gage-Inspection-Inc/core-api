from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.workflow.definition import (
    WorkflowDefinition as WorkflowDefinition,
)

class WorkflowDeploymentService(Entity):
    def get_definition(self, definition_id): ...
    def enumerate_definitions(self, published_only: bool = False): ...
    @property
    def entity_type_name(self): ...
