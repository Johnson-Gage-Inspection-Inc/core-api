from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.compat import is_string_type as is_string_type
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.service_operation import ServiceOperationPath as ServiceOperationPath

class ODataPathBuilder:
    @staticmethod
    def parse_url(path_str: str) -> ResourcePath: ...
    @staticmethod
    def build_segment(path: ServiceOperationPath) -> str: ...
