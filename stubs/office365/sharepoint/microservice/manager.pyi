from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity

class MicroServiceManager(Entity):
    @staticmethod
    def add_microservice_work_item(context, payload, minutes, properties): ...
    @property
    def entity_type_name(self): ...
