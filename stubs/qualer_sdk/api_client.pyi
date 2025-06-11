from _typeshed import Incomplete
from qualer_sdk import rest as rest
from qualer_sdk.api_response import ApiResponse as ApiResponse
from qualer_sdk.configuration import Configuration as Configuration
from qualer_sdk.exceptions import (
    ApiException as ApiException,
    ApiValueError as ApiValueError,
)

class ApiClient:
    PRIMITIVE_TYPES: Incomplete
    NATIVE_TYPES_MAPPING: Incomplete
    configuration: Incomplete
    pool_threads: Incomplete
    rest_client: Incomplete
    default_headers: Incomplete
    cookie: Incomplete
    client_side_validation: Incomplete
    def __init__(
        self,
        configuration: Incomplete | None = None,
        header_name: Incomplete | None = None,
        header_value: Incomplete | None = None,
        cookie: Incomplete | None = None,
        pool_threads: int = 1,
    ) -> None: ...
    def __enter__(self): ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def pool(self): ...
    @property
    def user_agent(self): ...
    @user_agent.setter
    def user_agent(self, value) -> None: ...
    def set_default_header(self, header_name, header_value) -> None: ...
    @classmethod
    def get_default(cls): ...
    @classmethod
    def set_default(cls, default) -> None: ...
    def sanitize_for_serialization(self, obj): ...
    def deserialize(self, response, response_type): ...
    def call_api(
        self,
        resource_path,
        method,
        path_params: Incomplete | None = None,
        query_params: Incomplete | None = None,
        header_params: Incomplete | None = None,
        body: Incomplete | None = None,
        post_params: Incomplete | None = None,
        files: Incomplete | None = None,
        response_types_map: Incomplete | None = None,
        auth_settings: Incomplete | None = None,
        async_req: Incomplete | None = None,
        _return_http_data_only: Incomplete | None = None,
        collection_formats: Incomplete | None = None,
        _preload_content: bool = True,
        _request_timeout: Incomplete | None = None,
        _host: Incomplete | None = None,
        _request_auth: Incomplete | None = None,
    ): ...
    def request(
        self,
        method,
        url,
        query_params: Incomplete | None = None,
        headers: Incomplete | None = None,
        post_params: Incomplete | None = None,
        body: Incomplete | None = None,
        _preload_content: bool = True,
        _request_timeout: Incomplete | None = None,
    ): ...
    def parameters_to_tuples(self, params, collection_formats): ...
    def parameters_to_url_query(self, params, collection_formats): ...
    def files_parameters(self, files: Incomplete | None = None): ...
    def select_header_accept(self, accepts): ...
    def select_header_content_type(self, content_types): ...
    def update_params_for_auth(
        self,
        headers,
        queries,
        auth_settings,
        resource_path,
        method,
        body,
        request_auth: Incomplete | None = None,
    ) -> None: ...
