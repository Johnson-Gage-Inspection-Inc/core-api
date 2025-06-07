from _typeshed import Incomplete
from office365.directory.policies.admin_consent_request import (
    AdminConsentRequestPolicy as AdminConsentRequestPolicy,
)
from office365.directory.policies.app_management import (
    AppManagementPolicy as AppManagementPolicy,
)
from office365.directory.policies.authentication_flows import (
    AuthenticationFlowsPolicy as AuthenticationFlowsPolicy,
)
from office365.directory.policies.authentication_methods import (
    AuthenticationMethodsPolicy as AuthenticationMethodsPolicy,
)
from office365.directory.policies.authentication_strength import (
    AuthenticationStrengthPolicy as AuthenticationStrengthPolicy,
)
from office365.directory.policies.authorization import (
    AuthorizationPolicy as AuthorizationPolicy,
)
from office365.directory.policies.conditional_access import (
    ConditionalAccessPolicy as ConditionalAccessPolicy,
)
from office365.directory.policies.cross_tenant_access import (
    CrossTenantAccessPolicy as CrossTenantAccessPolicy,
)
from office365.directory.policies.device_registration import (
    DeviceRegistrationPolicy as DeviceRegistrationPolicy,
)
from office365.directory.policies.feature_rollout import (
    FeatureRolloutPolicy as FeatureRolloutPolicy,
)
from office365.directory.policies.permission_grant import (
    PermissionGrantPolicy as PermissionGrantPolicy,
)
from office365.directory.policies.tenant_app_management import (
    TenantAppManagementPolicy as TenantAppManagementPolicy,
)
from office365.directory.policies.unified_role_management import (
    UnifiedRoleManagementPolicy as UnifiedRoleManagementPolicy,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class PolicyRoot(Entity):
    @property
    def admin_consent_request_policy(self): ...
    @property
    def authentication_methods_policy(self): ...
    @property
    def authentication_strength_policies(
        self,
    ) -> EntityCollection[AuthenticationStrengthPolicy]: ...
    @property
    def authentication_flows_policy(self): ...
    @property
    def authorization_policy(self): ...
    @property
    def app_management_policies(self) -> EntityCollection[AppManagementPolicy]: ...
    @property
    def conditional_access_policies(
        self,
    ) -> EntityCollection[ConditionalAccessPolicy]: ...
    @property
    def cross_tenant_access_policy(self): ...
    @property
    def device_registration_policy(self): ...
    @property
    def default_app_management_policy(self): ...
    @property
    def feature_rollout_policies(self) -> EntityCollection[FeatureRolloutPolicy]: ...
    @property
    def permission_grant_policies(self) -> EntityCollection[PermissionGrantPolicy]: ...
    @property
    def role_management_policies(
        self,
    ) -> EntityCollection[UnifiedRoleManagementPolicy]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
