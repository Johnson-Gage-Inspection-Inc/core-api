from _typeshed import Incomplete
from office365.directory.licenses.service_plan_info import (
    ServicePlanInfo as ServicePlanInfo,
)
from office365.entity import Entity as Entity
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class LicenseDetails(Entity):
    @property
    def service_plans(self): ...
    @property
    def sku_id(self) -> str | None: ...
    @property
    def sku_part_number(self) -> str | None: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
