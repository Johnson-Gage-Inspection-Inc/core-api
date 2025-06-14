from _typeshed import Incomplete
from office365.directory.licenses.service_plan_info import (
    ServicePlanInfo as ServicePlanInfo,
)
from office365.directory.licenses.units_detail import (
    LicenseUnitsDetail as LicenseUnitsDetail,
)
from office365.entity import Entity as Entity
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class SubscribedSku(Entity):
    @property
    def account_id(self) -> str | None: ...
    @property
    def applies_to(self) -> str | None: ...
    @property
    def sku_id(self) -> str | None: ...
    @property
    def sku_part_number(self) -> str | None: ...
    @property
    def prepaid_units(self): ...
    @property
    def service_plans(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
