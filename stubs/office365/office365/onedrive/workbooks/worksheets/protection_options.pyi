from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class WorkbookWorksheetProtectionOptions(ClientValue):
    allowAutoFilter: Incomplete
    allowDeleteColumns: Incomplete
    allowDeleteRows: Incomplete
    allowFormatCells: Incomplete
    allowFormatColumns: Incomplete
    allowFormatRows: Incomplete
    allowInsertColumns: Incomplete
    allowInsertHyperlinks: Incomplete
    allowInsertRows: Incomplete
    allowPivotTables: Incomplete
    allowSort: Incomplete
    def __init__(
        self,
        allow_auto_filter: Incomplete | None = None,
        allow_delete_columns: Incomplete | None = None,
        allow_delete_rows: Incomplete | None = None,
        allow_format_cells: Incomplete | None = None,
        allow_format_columns: Incomplete | None = None,
        allow_format_rows: Incomplete | None = None,
        allow_insert_columns: Incomplete | None = None,
        allow_insert_hyperlinks: Incomplete | None = None,
        allow_insert_rows: Incomplete | None = None,
        allow_pivot_tables: Incomplete | None = None,
        allow_sort: Incomplete | None = None,
    ) -> None: ...
