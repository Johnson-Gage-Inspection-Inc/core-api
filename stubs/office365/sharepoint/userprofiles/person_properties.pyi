from _typeshed import Incomplete
from office365.runtime.odata.type import ODataType as ODataType
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.entity import Entity as Entity

class PersonProperties(Entity):
    @property
    def account_name(self) -> str | None: ...
    @property
    def email(self) -> str | None: ...
    @property
    def latest_post(self) -> str | None: ...
    @property
    def peers(self): ...
    @property
    def personal_url(self) -> str | None: ...
    @property
    def extended_managers(self): ...
    @property
    def extended_reports(self): ...
    @property
    def picture_url(self) -> str | None: ...
    @property
    def user_url(self) -> str | None: ...
    @property
    def user_profile_properties(self): ...
    @property
    def entity_type_name(self): ...
    def set_property(self, k, v, persist_changes: bool = True): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
