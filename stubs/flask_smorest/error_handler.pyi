import marshmallow as ma
from _typeshed import Incomplete

class ErrorSchema(ma.Schema):
    code: Incomplete
    status: Incomplete
    message: Incomplete
    errors: Incomplete

class ErrorHandlerMixin:
    ERROR_SCHEMA = ErrorSchema
    def handle_http_exception(self, error): ...
