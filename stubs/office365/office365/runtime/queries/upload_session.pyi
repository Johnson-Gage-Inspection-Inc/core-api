from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.odata.v4.upload_session import UploadSession as UploadSession
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)

class UploadSessionQuery(ServiceOperationQuery):
    def __init__(self, binding_type, parameters_type) -> None: ...
    @property
    def upload_session_url(self): ...
    @property
    def return_type(self) -> ClientResult[UploadSession]: ...
