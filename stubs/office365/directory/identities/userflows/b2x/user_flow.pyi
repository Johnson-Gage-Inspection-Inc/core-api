from _typeshed import Incomplete
from office365.directory.identities.userflows.language_configuration import UserFlowLanguageConfiguration as UserFlowLanguageConfiguration
from office365.directory.identities.userflows.user_attribute_assignment import IdentityUserFlowAttributeAssignmentCollection as IdentityUserFlowAttributeAssignmentCollection
from office365.directory.identities.userflows.user_flow import IdentityUserFlow as IdentityUserFlow
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class B2XIdentityUserFlow(IdentityUserFlow):
    @property
    def languages(self) -> EntityCollection[UserFlowLanguageConfiguration]: ...
    @property
    def user_attribute_assignments(self) -> IdentityUserFlowAttributeAssignmentCollection: ...
    @property
    def user_flow_type(self) -> str | None: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
