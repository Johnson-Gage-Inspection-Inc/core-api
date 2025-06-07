from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.administration.web_application import WebApplication as WebApplication
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection

class SPWebService(Entity):
    @staticmethod
    def content_service(context): ...
    @property
    def web_applications(self): ...
    @property
    def entity_type_name(self): ...
