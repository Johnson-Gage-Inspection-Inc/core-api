from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.tenant.administration.webs.templates.template import SPOTenantWebTemplate as SPOTenantWebTemplate

class SPOTenantWebTemplateCollection(Entity):
    @property
    def items(self): ...
