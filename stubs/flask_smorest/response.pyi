from .utils import (
    deepupdate as deepupdate,
    get_appcontext as get_appcontext,
    prepare_response as prepare_response,
    remove_none as remove_none,
    resolve_schema_instance as resolve_schema_instance,
    set_status_and_headers_in_response as set_status_and_headers_in_response,
    unpack_tuple_response as unpack_tuple_response,
)
from _typeshed import Incomplete

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
