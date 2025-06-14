from _typeshed import Incomplete
from office365.runtime.odata.json_format import ODataJsonFormat as ODataJsonFormat
from office365.runtime.odata.v3.metadata_level import (
    ODataV3MetadataLevel as ODataV3MetadataLevel,
)

class JsonLightFormat(ODataJsonFormat):
    function: Incomplete
    def __init__(self, metadata_level=...) -> None: ...
    @property
    def security(self): ...
    @property
    def collection(self): ...
    @property
    def collection_next(self): ...
    @property
    def collection_delta(self): ...
    @property
    def metadata_type(self): ...
    @property
    def deferred_type(self): ...
    @property
    def value_tag(self): ...
    @property
    def etag(self): ...
    @property
    def media_type(self): ...
    @property
    def include_control_information(self): ...
