from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class SecondaryAdministratorsFieldsData(ClientValue):
    secondaryAdministratorEmails: Incomplete
    secondaryAdministratorLoginNames: Incomplete
    siteId: Incomplete
    def __init__(
        self,
        site_id: Incomplete | None = None,
        emails: Incomplete | None = None,
        names: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
