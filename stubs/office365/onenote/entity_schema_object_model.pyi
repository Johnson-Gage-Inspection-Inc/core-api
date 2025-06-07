from _typeshed import Incomplete
from datetime import datetime
from office365.onenote.entity_base_model import OnenoteEntityBaseModel as OnenoteEntityBaseModel

class OnenoteEntitySchemaObjectModel(OnenoteEntityBaseModel):
    @property
    def created_datetime(self) -> datetime | None: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
