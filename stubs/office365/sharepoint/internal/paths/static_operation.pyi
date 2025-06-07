from office365.runtime.paths.service_operation import ServiceOperationPath as ServiceOperationPath

class StaticOperationPath(ServiceOperationPath):
    def __init__(self, static_name: str, parameters: dict | None = None) -> None: ...
