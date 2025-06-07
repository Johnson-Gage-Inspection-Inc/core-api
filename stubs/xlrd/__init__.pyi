from .formula import *
from .biffh import XL_CELL_BLANK as XL_CELL_BLANK, XL_CELL_BOOLEAN as XL_CELL_BOOLEAN, XL_CELL_DATE as XL_CELL_DATE, XL_CELL_EMPTY as XL_CELL_EMPTY, XL_CELL_ERROR as XL_CELL_ERROR, XL_CELL_NUMBER as XL_CELL_NUMBER, XL_CELL_TEXT as XL_CELL_TEXT, biff_text_from_num as biff_text_from_num, error_text_from_code as error_text_from_code
from .book import colname as colname
from .info import __VERSION__ as __VERSION__, __version__ as __version__
from .sheet import empty_cell as empty_cell
from .xldate import XLDateError as XLDateError, xldate_as_datetime as xldate_as_datetime, xldate_as_tuple as xldate_as_tuple
from _typeshed import Incomplete

FILE_FORMAT_DESCRIPTIONS: Incomplete
ZIP_SIGNATURE: bytes
PEEK_SIZE: Incomplete

def inspect_format(path: Incomplete | None = None, content: Incomplete | None = None): ...
def open_workbook(filename: Incomplete | None = None, logfile=..., verbosity: int = 0, use_mmap: bool = True, file_contents: Incomplete | None = None, encoding_override: Incomplete | None = None, formatting_info: bool = False, on_demand: bool = False, ragged_rows: bool = False, ignore_workbook_corruption: bool = False): ...
def dump(filename, outfile=..., unnumbered: bool = False) -> None: ...
def count_records(filename, outfile=...) -> None: ...
