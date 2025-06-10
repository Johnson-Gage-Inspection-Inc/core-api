from office365.entity import Entity as Entity
from office365.partners.billing.azure_usage import AzureUsage as AzureUsage
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Billing(Entity):
    @property
    def usage(self): ...
