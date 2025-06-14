from office365.runtime.odata.model import ODataModel as ODataModel
from office365.runtime.odata.property import ODataProperty as ODataProperty
from office365.runtime.odata.type import ODataType as ODataType

class ODataReader:
    def __init__(self, metadata_path, xml_namespaces) -> None: ...
    def format_file(self) -> None: ...
    def process_schema_node(self, model) -> None: ...
    def process_type_node(self, type_node, schema_node): ...
    def process_method_node(self) -> None: ...
    def process_property_node(self, node): ...
    def generate_model(self): ...
