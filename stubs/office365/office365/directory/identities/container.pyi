from _typeshed import Incomplete
from office365.directory.authentication.conditions.event_listener import (
    AuthenticationEventListener as AuthenticationEventListener,
)
from office365.directory.identities.api_connector import (
    IdentityApiConnector as IdentityApiConnector,
)
from office365.directory.identities.conditional_access_root import (
    ConditionalAccessRoot as ConditionalAccessRoot,
)
from office365.directory.identities.providers.base_collection import (
    IdentityProviderBaseCollection as IdentityProviderBaseCollection,
)
from office365.directory.identities.userflows.attribute import (
    IdentityUserFlowAttribute as IdentityUserFlowAttribute,
)
from office365.directory.identities.userflows.b2x.user_flow import (
    B2XIdentityUserFlow as B2XIdentityUserFlow,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class IdentityContainer(Entity):
    @property
    def api_connectors(self) -> EntityCollection[IdentityApiConnector]: ...
    @property
    def authentication_event_listeners(
        self,
    ) -> EntityCollection[AuthenticationEventListener]: ...
    @property
    def conditional_access(self): ...
    @property
    def identity_providers(self): ...
    @property
    def b2x_user_flows(self): ...
    @property
    def user_flow_attributes(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
