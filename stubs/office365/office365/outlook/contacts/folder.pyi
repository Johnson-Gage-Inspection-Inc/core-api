from _typeshed import Incomplete
from office365.directory.extensions.extended_property import (
    MultiValueLegacyExtendedProperty as MultiValueLegacyExtendedProperty,
    SingleValueLegacyExtendedProperty as SingleValueLegacyExtendedProperty,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class ContactFolder(Entity):
    @property
    def contacts(self): ...
    @property
    def child_folders(self) -> EntityCollection["ContactFolder"]: ...
    @property
    def multi_value_extended_properties(
        self,
    ) -> EntityCollection[MultiValueLegacyExtendedProperty]: ...
    @property
    def single_value_extended_properties(
        self,
    ) -> EntityCollection[SingleValueLegacyExtendedProperty]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
