from _typeshed import Incomplete
from office365.directory.extensions.extended_property import (
    MultiValueLegacyExtendedProperty as MultiValueLegacyExtendedProperty,
)
from office365.directory.extensions.extended_property import (
    SingleValueLegacyExtendedProperty as SingleValueLegacyExtendedProperty,
)
from office365.directory.extensions.extension import Extension as Extension
from office365.directory.profile_photo import ProfilePhoto as ProfilePhoto
from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.calendar.email_address import EmailAddress as EmailAddress
from office365.outlook.item import OutlookItem as OutlookItem
from office365.outlook.mail.physical_address import PhysicalAddress as PhysicalAddress
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.types.collections import StringCollection as StringCollection

class Contact(OutlookItem):
    @property
    def business_phones(self): ...
    @property
    def display_name(self) -> str | None: ...
    @property
    def manager(self) -> str | None: ...
    @manager.setter
    def manager(self, value: str) -> None: ...
    @property
    def mobile_phone(self) -> str | None: ...
    @mobile_phone.setter
    def mobile_phone(self, value: str) -> None: ...
    @property
    def home_address(self): ...
    @property
    def email_addresses(self) -> ClientValueCollection[EmailAddress]: ...
    @property
    def extensions(self) -> EntityCollection[Extension]: ...
    @property
    def photo(self): ...
    @property
    def multi_value_extended_properties(
        self,
    ) -> EntityCollection[MultiValueLegacyExtendedProperty]: ...
    @property
    def single_value_extended_properties(
        self,
    ) -> EntityCollection[SingleValueLegacyExtendedProperty]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
