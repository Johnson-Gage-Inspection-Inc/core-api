from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class QueryPropertyValue(ClientValue):
    BoolVal: Incomplete
    IntVal: Incomplete
    StrArray: Incomplete
    StrVal: Incomplete
    QueryPropertyValueTypeIndex: Incomplete
    def __init__(
        self,
        bool_val: Incomplete | None = None,
        int_val: Incomplete | None = None,
        str_array: Incomplete | None = None,
        str_val: Incomplete | None = None,
        query_property_value_type_index: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
