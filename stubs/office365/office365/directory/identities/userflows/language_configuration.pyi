from _typeshed import Incomplete
from office365.directory.identities.userflows.language_page import (
    UserFlowLanguagePage as UserFlowLanguagePage,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class UserFlowLanguageConfiguration(Entity):
    @property
    def display_name(self) -> str | None: ...
    @property
    def default_pages(self) -> EntityCollection[UserFlowLanguagePage]: ...
    @property
    def overrides_pages(self) -> EntityCollection[UserFlowLanguagePage]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
