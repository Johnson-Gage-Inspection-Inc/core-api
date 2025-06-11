from _typeshed import Incomplete

JSON_SCHEMA_VALIDATION_KEYWORDS: Incomplete

class Configuration:
    server_index: Incomplete
    server_operation_index: Incomplete
    server_variables: Incomplete
    server_operation_variables: Incomplete
    temp_folder_path: Incomplete
    api_key: Incomplete
    api_key_prefix: Incomplete
    refresh_api_key_hook: Incomplete
    username: Incomplete
    password: Incomplete
    access_token: Incomplete
    logger: Incomplete
    logger_stream_handler: Incomplete
    logger_file_handler: Incomplete
    verify_ssl: bool
    ssl_ca_cert: Incomplete
    cert_file: Incomplete
    key_file: Incomplete
    assert_hostname: Incomplete
    tls_server_name: Incomplete
    connection_pool_maxsize: Incomplete
    proxy: Incomplete
    proxy_headers: Incomplete
    safe_chars_for_path_param: str
    retries: Incomplete
    client_side_validation: bool
    socket_options: Incomplete
    datetime_format: str
    date_format: str
    def __init__(
        self,
        host: Incomplete | None = None,
        api_key: Incomplete | None = None,
        api_key_prefix: Incomplete | None = None,
        username: Incomplete | None = None,
        password: Incomplete | None = None,
        access_token: Incomplete | None = None,
        server_index: Incomplete | None = None,
        server_variables: Incomplete | None = None,
        server_operation_index: Incomplete | None = None,
        server_operation_variables: Incomplete | None = None,
        ssl_ca_cert: Incomplete | None = None,
    ) -> None: ...
    def __deepcopy__(self, memo): ...
    def __setattr__(self, name, value) -> None: ...
    @classmethod
    def set_default(cls, default) -> None: ...
    @classmethod
    def get_default_copy(cls): ...
    @classmethod
    def get_default(cls): ...
    @property
    def logger_file(self): ...
    @logger_file.setter
    def logger_file(self, value) -> None: ...
    @property
    def debug(self): ...
    @debug.setter
    def debug(self, value) -> None: ...
    @property
    def logger_format(self): ...
    logger_formatter: Incomplete
    @logger_format.setter
    def logger_format(self, value) -> None: ...
    def get_api_key_with_prefix(self, identifier, alias: Incomplete | None = None): ...
    def get_basic_auth_token(self): ...
    def auth_settings(self): ...
    def to_debug_report(self): ...
    def get_host_settings(self): ...
    def get_host_from_settings(
        self,
        index,
        variables: Incomplete | None = None,
        servers: Incomplete | None = None,
    ): ...
    @property
    def host(self): ...
    @host.setter
    def host(self, value) -> None: ...
