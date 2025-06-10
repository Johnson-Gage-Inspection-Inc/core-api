from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SocialPostCreationData(ClientValue):
    ContentText: Incomplete
    def __init__(self, content_text: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
