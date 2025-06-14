import datetime

from _typeshed import Incomplete
from office365.runtime.odata.type import ODataType as ODataType
from office365.sharepoint.changes.token import ChangeToken as ChangeToken
from office365.sharepoint.changes.type import ChangeType as ChangeType
from office365.sharepoint.entity import Entity as Entity

class Change(Entity):
    @property
    def change_type_name(self): ...
    @property
    def change_token(self): ...
    @property
    def change_type(self): ...
    @property
    def site_id(self) -> str | None: ...
    @property
    def time(self) -> datetime.datetime: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
