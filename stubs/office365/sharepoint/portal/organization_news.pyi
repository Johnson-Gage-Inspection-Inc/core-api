from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity

class OrganizationNewsSiteReference(ClientValue): ...

class OrganizationNews(Entity):
    def sites_reference(self): ...
