from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.odata.type import ODataType as ODataType
from office365.sharepoint.principal.type import PrincipalType as PrincipalType

class PrincipalInfo(ClientValue):
    PrincipalId: Incomplete
    DisplayName: Incomplete
    Email: Incomplete
    LoginName: Incomplete
    Department: Incomplete
    JobTitle: Incomplete
    PrincipalType: Incomplete
    def __init__(self, principal_id: Incomplete | None = None, display_name: Incomplete | None = None, email: Incomplete | None = None, login_name: Incomplete | None = None, department: Incomplete | None = None, job_title: Incomplete | None = None, principal_type: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
    @property
    def principal_type_name(self): ...
