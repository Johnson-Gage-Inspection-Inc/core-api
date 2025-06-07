from office365.entity import Entity as Entity
from office365.partners.billing.billing import Billing as Billing
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Partners(Entity):
    @property
    def billing(self): ...
