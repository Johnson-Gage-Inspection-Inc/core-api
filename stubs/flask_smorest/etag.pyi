from .exceptions import NotModified as NotModified, PreconditionFailed as PreconditionFailed, PreconditionRequired as PreconditionRequired
from .globals import current_api as current_api
from .utils import deepupdate as deepupdate, get_appcontext as get_appcontext, resolve_schema_instance as resolve_schema_instance
from _typeshed import Incomplete

IF_NONE_MATCH_HEADER: Incomplete
IF_MATCH_HEADER: Incomplete
ETAG_HEADER: Incomplete

class EtagMixin:
    METHODS_CHECKING_NOT_MODIFIED: Incomplete
    METHODS_NEEDING_CHECK_ETAG: Incomplete
    METHODS_ALLOWING_SET_ETAG: Incomplete
    ETAG_INCLUDE_HEADERS: Incomplete
    def etag(self, obj): ...
    def check_etag(self, etag_data, etag_schema: Incomplete | None = None) -> None: ...
    def set_etag(self, etag_data, etag_schema: Incomplete | None = None) -> None: ...
