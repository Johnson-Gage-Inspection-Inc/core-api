from _typeshed import Incomplete

from .biffh import XL_CELL_BLANK as XL_CELL_BLANK
from .biffh import XL_CELL_BOOLEAN as XL_CELL_BOOLEAN
from .biffh import XL_CELL_DATE as XL_CELL_DATE
from .biffh import XL_CELL_EMPTY as XL_CELL_EMPTY
from .biffh import XL_CELL_ERROR as XL_CELL_ERROR
from .biffh import XL_CELL_NUMBER as XL_CELL_NUMBER
from .biffh import XL_CELL_TEXT as XL_CELL_TEXT
from .biffh import biff_text_from_num as biff_text_from_num
from .biffh import error_text_from_code as error_text_from_code
from .book import colname as colname
from .formula import *
from .info import __VERSION__ as __VERSION__
from .info import __version__ as __version__
from .sheet import empty_cell as empty_cell
from .xldate import XLDateError as XLDateError
from .xldate import xldate_as_datetime as xldate_as_datetime
from .xldate import xldate_as_tuple as xldate_as_tuple

FILE_FORMAT_DESCRIPTIONS: Incomplete
ZIP_SIGNATURE: bytes
PEEK_SIZE: Incomplete

def inspect_format(
    path: Incomplete | None = None, content: Incomplete | None = None
): ...
def open_workbook(
    filename: Incomplete | None = None,
    logfile=...,
    verbosity: int = 0,
    use_mmap: bool = True,
    file_contents: Incomplete | None = None,
    encoding_override: Incomplete | None = None,
    formatting_info: bool = False,
    on_demand: bool = False,
    ragged_rows: bool = False,
    ignore_workbook_corruption: bool = False,
): ...
def dump(filename, outfile=..., unnumbered: bool = False) -> None: ...
def count_records(filename, outfile=...) -> None: ...
