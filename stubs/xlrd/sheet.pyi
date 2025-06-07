from .biffh import *
from .timemachine import *
from .formatting import Format as Format, nearest_colour_index as nearest_colour_index
from .formula import FMLA_TYPE_CELL as FMLA_TYPE_CELL, FMLA_TYPE_SHARED as FMLA_TYPE_SHARED, decompile_formula as decompile_formula, dump_formula as dump_formula, rangename2d as rangename2d
from _typeshed import Incomplete

DEBUG: int
OBJ_MSO_DEBUG: int

class Sheet(BaseObject):
    name: str
    book: Incomplete
    nrows: int
    ncols: int
    colinfo_map: Incomplete
    rowinfo_map: Incomplete
    col_label_ranges: Incomplete
    row_label_ranges: Incomplete
    merged_cells: Incomplete
    rich_text_runlist_map: Incomplete
    defcolwidth: Incomplete
    standardwidth: Incomplete
    default_row_height: Incomplete
    default_row_height_mismatch: Incomplete
    default_row_hidden: Incomplete
    default_additional_space_above: Incomplete
    default_additional_space_below: Incomplete
    visibility: int
    gcw: Incomplete
    hyperlink_list: Incomplete
    hyperlink_map: Incomplete
    cell_note_map: Incomplete
    vert_split_pos: int
    horz_split_pos: int
    horz_split_first_visible: int
    vert_split_first_visible: int
    split_active_pane: int
    has_pane_record: int
    horizontal_page_breaks: Incomplete
    vertical_page_breaks: Incomplete
    biff_version: Incomplete
    logfile: Incomplete
    bt: Incomplete
    bf: Incomplete
    number: Incomplete
    verbosity: Incomplete
    formatting_info: Incomplete
    ragged_rows: Incomplete
    put_cell: Incomplete
    first_visible_rowx: int
    first_visible_colx: int
    gridline_colour_index: int
    gridline_colour_rgb: Incomplete
    cooked_page_break_preview_mag_factor: int
    cooked_normal_view_mag_factor: int
    cached_page_break_preview_mag_factor: int
    cached_normal_view_mag_factor: int
    scl_mag_factor: Incomplete
    utter_max_rows: int
    utter_max_cols: int
    def __init__(self, book, position, name, number) -> None: ...
    def cell(self, rowx, colx): ...
    def cell_value(self, rowx, colx): ...
    def cell_type(self, rowx, colx): ...
    def cell_xf_index(self, rowx, colx): ...
    def row_len(self, rowx): ...
    def row(self, rowx): ...
    def __getitem__(self, item): ...
    def get_rows(self): ...
    __iter__ = get_rows
    def row_types(self, rowx, start_colx: int = 0, end_colx: Incomplete | None = None): ...
    def row_values(self, rowx, start_colx: int = 0, end_colx: Incomplete | None = None): ...
    def row_slice(self, rowx, start_colx: int = 0, end_colx: Incomplete | None = None): ...
    def col_slice(self, colx, start_rowx: int = 0, end_rowx: Incomplete | None = None): ...
    def col_values(self, colx, start_rowx: int = 0, end_rowx: Incomplete | None = None): ...
    def col_types(self, colx, start_rowx: int = 0, end_rowx: Incomplete | None = None): ...
    col = col_slice
    def tidy_dimensions(self) -> None: ...
    def put_cell_ragged(self, rowx, colx, ctype, value, xf_index) -> None: ...
    def put_cell_unragged(self, rowx, colx, ctype, value, xf_index) -> None: ...
    def read(self, bk): ...
    def string_record_contents(self, data): ...
    def update_cooked_mag_factors(self) -> None: ...
    def fixed_BIFF2_xfindex(self, cell_attr, rowx, colx, true_xfx: Incomplete | None = None): ...
    def insert_new_BIFF20_xf(self, cell_attr, style: int = 0): ...
    def fake_XF_from_BIFF20_cell_attr(self, cell_attr, style: int = 0): ...
    def req_fmt_info(self) -> None: ...
    def computed_column_width(self, colx): ...
    def handle_hlink(self, data): ...
    def handle_quicktip(self, data) -> None: ...
    def handle_msodrawingetc(self, recid, data_len, data) -> None: ...
    def handle_obj(self, data): ...
    def handle_note(self, data, txos) -> None: ...
    def handle_txo(self, data): ...
    def handle_feat11(self, data) -> None: ...

class MSODrawing(BaseObject): ...
class MSObj(BaseObject): ...
class MSTxo(BaseObject): ...

class Note(BaseObject):
    author: Incomplete
    col_hidden: int
    colx: int
    rich_text_runlist: Incomplete
    row_hidden: int
    rowx: int
    show: int
    text: Incomplete

class Hyperlink(BaseObject):
    frowx: Incomplete
    lrowx: Incomplete
    fcolx: Incomplete
    lcolx: Incomplete
    type: Incomplete
    url_or_path: Incomplete
    desc: Incomplete
    target: Incomplete
    textmark: Incomplete
    quicktip: Incomplete

def unpack_RK(rk_str): ...

cellty_from_fmtty: Incomplete
ctype_text: Incomplete

class Cell(BaseObject):
    ctype: Incomplete
    value: Incomplete
    xf_index: Incomplete
    def __init__(self, ctype, value, xf_index: Incomplete | None = None) -> None: ...

empty_cell: Incomplete

class Colinfo(BaseObject):
    width: int
    xf_index: int
    hidden: int
    bit1_flag: int
    outline_level: int
    collapsed: int

class Rowinfo(BaseObject):
    height: Incomplete
    has_default_height: Incomplete
    outline_level: Incomplete
    outline_group_starts_ends: Incomplete
    hidden: Incomplete
    height_mismatch: Incomplete
    has_default_xf_index: Incomplete
    xf_index: Incomplete
    additional_space_above: Incomplete
    additional_space_below: Incomplete
    def __init__(self) -> None: ...
