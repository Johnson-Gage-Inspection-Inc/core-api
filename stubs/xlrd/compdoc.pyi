from _typeshed import Incomplete

from .timemachine import *

SIGNATURE: bytes
EOCSID: int
FREESID: int
SATSID: int
MSATSID: int
EVILSID: int

class CompDocError(Exception): ...

class DirNode:
    DID: Incomplete
    logfile: Incomplete
    name: Incomplete
    children: Incomplete
    parent: int
    tsinfo: Incomplete
    def __init__(self, DID, dent, DEBUG: int = 0, logfile=...) -> None: ...
    def dump(self, DEBUG: int = 1) -> None: ...

class CompDoc:
    logfile: Incomplete
    ignore_workbook_corruption: Incomplete
    DEBUG: Incomplete
    mem: Incomplete
    sec_size: Incomplete
    short_sec_size: Incomplete
    mem_data_secs: Incomplete
    mem_data_len: Incomplete
    SAT: Incomplete
    dirlist: Incomplete
    SSCS: str
    SSAT: Incomplete
    def __init__(
        self, mem, logfile=..., DEBUG: int = 0, ignore_workbook_corruption: bool = False
    ) -> None: ...
    def get_named_stream(self, qname): ...
    def locate_named_stream(self, qname): ...

def x_dump_line(alist, stride, f, dpos, equal: int = 0) -> None: ...
def dump_list(alist, stride, f=...) -> None: ...
