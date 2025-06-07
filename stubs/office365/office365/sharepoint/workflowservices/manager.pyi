from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity

class WorkflowServicesManager(Entity):
    def get_workflow_instance_service(self): ...
    @staticmethod
    def current(context): ...
    @property
    def entity_type_name(self): ...
