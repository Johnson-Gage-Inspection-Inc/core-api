from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.workflowservices.instance import WorkflowInstance as WorkflowInstance

class WorkflowInstanceService(Entity):
    def enumerate_instances_for_site(self): ...
    @property
    def entity_type_name(self): ...
