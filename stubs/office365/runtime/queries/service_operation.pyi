from _typeshed import Incomplete
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.client_query import ClientQuery as ClientQuery, T as T

class ServiceOperationQuery(ClientQuery[T]):
    static: Incomplete
    def __init__(
        self,
        binding_type,
        method_name: Incomplete | None = None,
        method_params: Incomplete | None = None,
        parameters_type: Incomplete | None = None,
        parameters_name: Incomplete | None = None,
        return_type: Incomplete | None = None,
        is_static: bool = False,
    ) -> None: ...
    @property
    def path(self): ...
    @property
    def url(self): ...
    @property
    def name(self): ...
