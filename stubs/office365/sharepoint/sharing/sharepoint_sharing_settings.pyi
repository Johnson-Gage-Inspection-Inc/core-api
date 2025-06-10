from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.sharing.picker_settings import (
    PickerSettings as PickerSettings,
)

class SharePointSharingSettings(Entity):
    @property
    def picker_properties(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
