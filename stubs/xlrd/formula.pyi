from .timemachine import *
from _typeshed import Incomplete

__all__ = ['oBOOL', 'oERR', 'oNUM', 'oREF', 'oREL', 'oSTRG', 'oUNK', 'decompile_formula', 'dump_formula', 'evaluate_name_formula', 'okind_dict', 'rangename3d', 'rangename3drel', 'cellname', 'cellnameabs', 'colname', 'FMLA_TYPE_CELL', 'FMLA_TYPE_SHARED', 'FMLA_TYPE_ARRAY', 'FMLA_TYPE_COND_FMT', 'FMLA_TYPE_DATA_VAL', 'FMLA_TYPE_NAME', 'Operand', 'Ref3D']

FMLA_TYPE_CELL: int
FMLA_TYPE_SHARED: int
FMLA_TYPE_ARRAY: int
FMLA_TYPE_COND_FMT: int
FMLA_TYPE_DATA_VAL: int
FMLA_TYPE_NAME: int
oBOOL: int
oERR: int
oNUM: int
oREF: int
oREL: int
oSTRG: int
oUNK: int
okind_dict: Incomplete

class FormulaError(Exception): ...

class Operand:
    value: Incomplete
    kind = oUNK
    text: str
    rank: Incomplete
    def __init__(self, akind: Incomplete | None = None, avalue: Incomplete | None = None, arank: int = 0, atext: str = '?') -> None: ...

class Ref3D(tuple):
    coords: Incomplete
    relflags: Incomplete
    def __init__(self, atuple) -> None: ...

def evaluate_name_formula(bk, nobj, namex, blah: int = 0, level: int = 0) -> None: ...
def decompile_formula(bk, fmla, fmlalen, fmlatype: Incomplete | None = None, browx: Incomplete | None = None, bcolx: Incomplete | None = None, blah: int = 0, level: int = 0, r1c1: int = 0): ...
def dump_formula(bk, data, fmlalen, bv, reldelta, blah: int = 0, isname: int = 0) -> None: ...
def cellname(rowx, colx): ...
def cellnameabs(rowx, colx, r1c1: int = 0): ...
def colname(colx): ...
def rangename3d(book, ref3d): ...
def rangename3drel(book, ref3d, browx: Incomplete | None = None, bcolx: Incomplete | None = None, r1c1: int = 0): ...
