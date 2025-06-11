import io
from _typeshed import Incomplete
from qualer_sdk.exceptions import (
    ApiException as ApiException,
    ApiValueError as ApiValueError,
    ForbiddenException as ForbiddenException,
    NotFoundException as NotFoundException,
    ServiceException as ServiceException,
    UnauthorizedException as UnauthorizedException,
)

logger: Incomplete

class RESTResponse(io.IOBase):
    urllib3_response: Incomplete
    status: Incomplete
    reason: Incomplete
    data: Incomplete
    def __init__(self, resp) -> None: ...
    def getheaders(self): ...
    def getheader(self, name, default: Incomplete | None = None): ...

class RESTClientObject:
    pool_manager: Incomplete
    def __init__(
        self, configuration, pools_size: int = 4, maxsize: Incomplete | None = None
    ) -> None: ...
    def request(
        self,
        method,
        url,
        query_params: Incomplete | None = None,
        headers: Incomplete | None = None,
        body: Incomplete | None = None,
        post_params: Incomplete | None = None,
        _preload_content: bool = True,
        _request_timeout: Incomplete | None = None,
    ): ...
    def get_request(
        self,
        url,
        headers: Incomplete | None = None,
        query_params: Incomplete | None = None,
        _preload_content: bool = True,
        _request_timeout: Incomplete | None = None,
    ): ...
    def head_request(
        self,
        url,
        headers: Incomplete | None = None,
        query_params: Incomplete | None = None,
        _preload_content: bool = True,
        _request_timeout: Incomplete | None = None,
    ): ...
    def options_request(
        self,
        url,
        headers: Incomplete | None = None,
        query_params: Incomplete | None = None,
        post_params: Incomplete | None = None,
        body: Incomplete | None = None,
        _preload_content: bool = True,
        _request_timeout: Incomplete | None = None,
    ): ...
    def delete_request(
        self,
        url,
        headers: Incomplete | None = None,
        query_params: Incomplete | None = None,
        body: Incomplete | None = None,
        _preload_content: bool = True,
        _request_timeout: Incomplete | None = None,
    ): ...
    def post_request(
        self,
        url,
        headers: Incomplete | None = None,
        query_params: Incomplete | None = None,
        post_params: Incomplete | None = None,
        body: Incomplete | None = None,
        _preload_content: bool = True,
        _request_timeout: Incomplete | None = None,
    ): ...
    def put_request(
        self,
        url,
        headers: Incomplete | None = None,
        query_params: Incomplete | None = None,
        post_params: Incomplete | None = None,
        body: Incomplete | None = None,
        _preload_content: bool = True,
        _request_timeout: Incomplete | None = None,
    ): ...
    def patch_request(
        self,
        url,
        headers: Incomplete | None = None,
        query_params: Incomplete | None = None,
        post_params: Incomplete | None = None,
        body: Incomplete | None = None,
        _preload_content: bool = True,
        _request_timeout: Incomplete | None = None,
    ): ...
