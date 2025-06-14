from _typeshed import Incomplete
from flask_smorest.exceptions import (
    MissingAPIParameterError as MissingAPIParameterError,
)
from flask_smorest.utils import normalize_config_prefix as normalize_config_prefix
from flask_smorest.utils import prepare_response as prepare_response

from .field_converters import uploadfield2properties as uploadfield2properties
from .plugins import FlaskPlugin as FlaskPlugin

HAS_PYYAML: bool

def delimited_list2param(self, field, **kwargs): ...

class DocBlueprintMixin: ...

class APISpecMixin(DocBlueprintMixin):
    DEFAULT_ERROR_RESPONSE_NAME: str
    DEFAULT_REQUEST_BODY_CONTENT_TYPE: str
    DEFAULT_RESPONSE_CONTENT_TYPE: str
    def register_converter(self, converter, func) -> None: ...
    def register_field(self, field, *args) -> None: ...

openapi_cli: Incomplete

def print_openapi_doc(format, config_prefix) -> None: ...
def write_openapi_doc(format, output_file, config_prefix) -> None: ...
def list_config_prefixes() -> None: ...
