from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.fields.lookup_value import FieldLookupValue as FieldLookupValue

class ListItemFormUpdateValue(ClientValue):
    FieldName: Incomplete
    FieldValue: Incomplete
    HasException: Incomplete
    ErrorCode: Incomplete
    ErrorMessage: Incomplete
    def __init__(self, name: Incomplete | None = None, value: Incomplete | None = None, has_exception: Incomplete | None = None, error_code: Incomplete | None = None, error_message: Incomplete | None = None) -> None: ...
    def to_json(self, json_format: Incomplete | None = None): ...
    @property
    def entity_type_name(self): ...
