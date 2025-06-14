from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.paths.builder import ODataPathBuilder as ODataPathBuilder
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class ServiceOperationPath(ResourcePath):
    def __init__(
        self,
        name: str,
        parameters: list | dict | ClientValue = None,
        parent: ResourcePath = None,
    ) -> None: ...
    @property
    def segment(self): ...
    @property
    def name(self): ...
    @property
    def parameters(self): ...
