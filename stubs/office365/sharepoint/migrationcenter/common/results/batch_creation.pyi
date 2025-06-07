from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class BatchCreationResult(ClientValue):
    CreatedCount: Incomplete
    CreatedTaskIdList: Incomplete
    ErrorCode: Incomplete
    ErrorMessage: Incomplete
    FieldError: Incomplete
    ProcessingMilliseconds: Incomplete
    TotalCount: Incomplete
    def __init__(self, created_count: Incomplete | None = None, created_task_id_list: Incomplete | None = None, error_code: Incomplete | None = None, error_message: Incomplete | None = None, field_error: Incomplete | None = None, processing_milliseconds: Incomplete | None = None, total_count: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self) -> str: ...
