from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class LookupColumn(ClientValue):
    listId: Incomplete
    columnName: Incomplete
    allowMultipleValues: Incomplete
    allowUnlimitedLength: Incomplete
    primaryLookupColumnId: Incomplete
    def __init__(self, list_id: Incomplete | None = None, column_name: Incomplete | None = None, allow_multiple_values: Incomplete | None = None, allow_unlimited_length: Incomplete | None = None, primary_lookup_column_id: Incomplete | None = None) -> None: ...
