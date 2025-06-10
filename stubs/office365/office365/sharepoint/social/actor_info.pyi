from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SocialActorInfo(ClientValue):
    AccountName: Incomplete
    def __init__(self, account_name: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
