from _typeshed import Incomplete

class OpenApiException(Exception): ...

class ApiException(OpenApiException):
    status: Incomplete
    reason: Incomplete
    http_resp: Incomplete
    body: Incomplete
    headers: Incomplete
    def __init__(
        self,
        status: Incomplete | None = None,
        reason: Incomplete | None = None,
        http_resp: Incomplete | None = None,
    ) -> None: ...

class ApiValueError(OpenApiException, ValueError): ...
class ApiTypeError(OpenApiException, TypeError): ...
class ApiKeyError(OpenApiException, KeyError): ...
class ApiAttributeError(OpenApiException, AttributeError): ...

class UnauthorizedException(ApiException):
    def __init__(self, http_resp: Incomplete | None = None) -> None: ...

class ForbiddenException(ApiException):
    def __init__(self, http_resp: Incomplete | None = None) -> None: ...

class NotFoundException(ApiException):
    def __init__(self, http_resp: Incomplete | None = None) -> None: ...

class ServiceException(ApiException):
    def __init__(
        self,
        status: Incomplete | None = None,
        reason: Incomplete | None = None,
        http_resp: Incomplete | None = None,
    ) -> None: ...
