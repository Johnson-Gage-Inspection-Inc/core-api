from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.intune.devices.category import DeviceCategory as DeviceCategory
from office365.intune.devices.compliance.policy_state import (
    DeviceCompliancePolicyState as DeviceCompliancePolicyState,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class ManagedDevice(Entity):
    def locate_device(self): ...
    @property
    def activation_lock_bypass_code(self) -> str | None: ...
    @property
    def device_category(self): ...
    @property
    def manufacturer(self) -> str | None: ...
    @property
    def operating_system(self) -> str | None: ...
    @property
    def device_compliance_policy_states(
        self,
    ) -> EntityCollection[DeviceCompliancePolicyState]: ...
    @property
    def users(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
