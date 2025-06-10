from office365.runtime.client_object import ClientObject as ClientObject
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.client_query import ClientQuery as ClientQuery, T as T

class FunctionQuery(ClientQuery[T]):
    def __init__(
        self,
        binding_type: ClientObject,
        method_name: str = None,
        method_params: list | dict | ClientValue = None,
        return_type: T = None,
    ) -> None: ...
    @property
    def path(self): ...
    @property
    def url(self): ...
    @property
    def name(self): ...
