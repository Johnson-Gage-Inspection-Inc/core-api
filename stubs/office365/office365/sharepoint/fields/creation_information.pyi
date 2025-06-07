from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.fields.type import FieldType as FieldType

class FieldCreationInformation(ClientValue):
    Title: Incomplete
    FieldTypeKind: Incomplete
    Description: Incomplete
    Choices: Incomplete
    LookupListId: Incomplete
    LookupFieldName: Incomplete
    LookupWebId: Incomplete
    Required: Incomplete
    Formula: Incomplete
    def __init__(
        self,
        title,
        field_type_kind,
        description: Incomplete | None = None,
        lookup_list_id: Incomplete | None = None,
        lookup_field_name: Incomplete | None = None,
        lookup_web_id: Incomplete | None = None,
        required: bool = False,
        formula: Incomplete | None = None,
        choices: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
