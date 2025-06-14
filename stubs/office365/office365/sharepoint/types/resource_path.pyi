from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.compat import (
    get_absolute_url as get_absolute_url,
    is_absolute_url as is_absolute_url,
    urlparse as urlparse,
)

class ResourcePath(ClientValue):
    DecodedUrl: Incomplete
    def __init__(self, decoded_url: Incomplete | None = None) -> None: ...
    @staticmethod
    def create_absolute(site_url, path): ...
    @staticmethod
    def create_relative(site_url, path): ...
    @property
    def entity_type_name(self): ...
