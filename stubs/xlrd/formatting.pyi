from _typeshed import Incomplete

from .biffh import FDT as FDT
from .biffh import FGE as FGE
from .biffh import FNU as FNU
from .biffh import FTX as FTX
from .biffh import FUN as FUN
from .biffh import XL_CELL_DATE as XL_CELL_DATE
from .biffh import XL_CELL_NUMBER as XL_CELL_NUMBER
from .biffh import XL_CELL_TEXT as XL_CELL_TEXT
from .biffh import XL_FORMAT as XL_FORMAT
from .biffh import XL_FORMAT2 as XL_FORMAT2
from .biffh import BaseObject as BaseObject
from .biffh import XLRDError as XLRDError
from .biffh import fprintf as fprintf
from .biffh import unpack_string as unpack_string
from .biffh import unpack_unicode as unpack_unicode
from .biffh import upkbits as upkbits
from .biffh import upkbitsL as upkbitsL
from .timemachine import *

DEBUG: int
excel_default_palette_b5: Incomplete
excel_default_palette_b2: Incomplete
excel_default_palette_b8: Incomplete
default_palette: Incomplete
built_in_style_names: Incomplete

def initialise_colour_map(book) -> None: ...
def nearest_colour_index(colour_map, rgb, debug: int = 0): ...

class EqNeAttrs:
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class Font(BaseObject, EqNeAttrs):
    bold: int
    character_set: int
    colour_index: int
    escapement: int
    family: int
    font_index: int
    height: int
    italic: int
    name: Incomplete
    struck_out: int
    underline_type: int
    underlined: int
    weight: int
    outline: int
    shadow: int

def handle_efont(book, data) -> None: ...
def handle_font(book, data) -> None: ...

class Format(BaseObject, EqNeAttrs):
    format_key: int
    type = FUN
    format_str: Incomplete
    def __init__(self, format_key, ty, format_str) -> None: ...

std_format_strings: Incomplete
fmt_code_ranges: Incomplete
std_format_code_types: Incomplete
date_chars: Incomplete
date_char_dict: Incomplete
skip_char_dict: Incomplete
num_char_dict: Incomplete
non_date_formats: Incomplete
fmt_bracketed_sub: Incomplete

def is_date_format_string(book, fmt): ...
def handle_format(self, data, rectype=...) -> None: ...
def handle_palette(book, data) -> None: ...
def palette_epilogue(book) -> None: ...
def handle_style(book, data) -> None: ...
def check_colour_indexes_in_obj(book, obj, orig_index) -> None: ...
def fill_in_standard_formats(book) -> None: ...
def handle_xf(self, data) -> None: ...
def xf_epilogue(self) -> None: ...
def initialise_book(book) -> None: ...

class XFBorder(BaseObject, EqNeAttrs):
    top_colour_index: int
    bottom_colour_index: int
    left_colour_index: int
    right_colour_index: int
    diag_colour_index: int
    top_line_style: int
    bottom_line_style: int
    left_line_style: int
    right_line_style: int
    diag_line_style: int
    diag_down: int
    diag_up: int

class XFBackground(BaseObject, EqNeAttrs):
    fill_pattern: int
    background_colour_index: int
    pattern_colour_index: int

class XFAlignment(BaseObject, EqNeAttrs):
    hor_align: int
    vert_align: int
    rotation: int
    text_wrapped: int
    indent_level: int
    shrink_to_fit: int
    text_direction: int

class XFProtection(BaseObject, EqNeAttrs):
    cell_locked: int
    formula_hidden: int

class XF(BaseObject):
    is_style: int
    parent_style_index: int
    xf_index: int
    font_index: int
    format_key: int
    protection: Incomplete
    background: Incomplete
    alignment: Incomplete
    border: Incomplete
