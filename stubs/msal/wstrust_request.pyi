from _typeshed import Incomplete

from .mex import Mex as Mex
from .wstrust_response import parse_response as parse_response

logger: Incomplete

def send_request(
    username,
    password,
    cloud_audience_urn,
    endpoint_address,
    soap_action,
    http_client,
    **kwargs,
): ...
def escape_password(password): ...
def wsu_time_format(datetime_obj): ...
