from _typeshed import Incomplete

from .utils import deepupdate as deepupdate
from .utils import get_appcontext as get_appcontext
from .utils import prepare_response as prepare_response
from .utils import remove_none as remove_none
from .utils import resolve_schema_instance as resolve_schema_instance
from .utils import (
    set_status_and_headers_in_response as set_status_and_headers_in_response,
)
from .utils import unpack_tuple_response as unpack_tuple_response

class ResponseMixin:
    def response(
        self,
        status_code,
        schema: Incomplete | None = None,
        *,
        content_type: Incomplete | None = None,
        description: Incomplete | None = None,
        example: Incomplete | None = None,
        examples: Incomplete | None = None,
        headers: Incomplete | None = None,
    ): ...
    def alt_response(
        self,
        status_code,
        response: Incomplete | None = None,
        *,
        schema: Incomplete | None = None,
        content_type: Incomplete | None = None,
        description: Incomplete | None = None,
        example: Incomplete | None = None,
        examples: Incomplete | None = None,
        headers: Incomplete | None = None,
        success: bool = False,
    ): ...
