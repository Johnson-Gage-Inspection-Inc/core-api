from _typeshed import Incomplete

from .exceptions import NotModified as NotModified
from .exceptions import PreconditionFailed as PreconditionFailed
from .exceptions import PreconditionRequired as PreconditionRequired
from .globals import current_api as current_api
from .utils import deepupdate as deepupdate
from .utils import get_appcontext as get_appcontext
from .utils import resolve_schema_instance as resolve_schema_instance

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
