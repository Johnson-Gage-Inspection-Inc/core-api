from office365.entity import Entity as Entity
from office365.partners.billing.billed_usage import BilledUsage as BilledUsage
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class AzureUsage(Entity):
    @property
    def billed(self): ...
