from _typeshed import Incomplete
from office365.directory.rolemanagement.role_permission import (
    RolePermission as RolePermission,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.intune.audit.event_collection import (
    AuditEventCollection as AuditEventCollection,
)
from office365.intune.brand import IntuneBrand as IntuneBrand
from office365.intune.devices.category import DeviceCategory as DeviceCategory
from office365.intune.devices.enrollment.configuration import (
    DeviceEnrollmentConfiguration as DeviceEnrollmentConfiguration,
)
from office365.intune.devices.managed import ManagedDevice as ManagedDevice
from office365.intune.devices.management.reports.reports import (
    DeviceManagementReports as DeviceManagementReports,
)
from office365.intune.devices.management.terms_and_conditions import (
    TermsAndConditions as TermsAndConditions,
)
from office365.intune.devices.management.virtual_endpoint import (
    VirtualEndpoint as VirtualEndpoint,
)
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

class DeviceManagement(Entity):
    def get_effective_permissions(self, scope: Incomplete | None = None): ...
    @property
    def audit_events(self): ...
    @property
    def virtual_endpoint(self): ...
    @property
    def terms_and_conditions(self): ...
    @property
    def device_categories(self): ...
    @property
    def device_enrollment_configurations(self): ...
    @property
    def intune_brand(self): ...
    @property
    def managed_devices(self): ...
    @property
    def reports(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
