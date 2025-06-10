from office365.sharepoint.publishing.customproperties.base import (
    BaseCustomProperty as BaseCustomProperty,
)

class BigIntCustomProperty(BaseCustomProperty):
    @property
    def entity_type_name(self): ...
