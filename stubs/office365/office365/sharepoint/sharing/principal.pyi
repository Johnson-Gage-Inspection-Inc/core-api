from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class Principal(ClientValue):
    id: Incomplete
    directoryObjectId: Incomplete
    email: Incomplete
    expiration: Incomplete
    isActive: Incomplete
    isExternal: Incomplete
    jobTitle: Incomplete
    loginName: Incomplete
    name: Incomplete
    def __init__(
        self,
        id_: Incomplete | None = None,
        directory_object_id: Incomplete | None = None,
        email: Incomplete | None = None,
        expiration: Incomplete | None = None,
        is_active: Incomplete | None = None,
        is_external: Incomplete | None = None,
        job_title: Incomplete | None = None,
        login_name: Incomplete | None = None,
        name: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
