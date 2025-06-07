from office365.onenote.operations.onenote_operation_error import OnenoteOperationError as OnenoteOperationError
from office365.onenote.operations.operation import Operation as Operation

class OnenoteOperation(Operation):
    @property
    def error(self): ...
