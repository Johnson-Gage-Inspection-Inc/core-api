from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ShareLinkRequest(ClientValue):
    linkKind: Incomplete
    expiration: Incomplete
    peoplePickerInput: Incomplete
    settings: Incomplete
    createLink: Incomplete
    def __init__(
        self,
        link_kind: Incomplete | None = None,
        expiration: Incomplete | None = None,
        people_picker_input: Incomplete | None = None,
        settings: Incomplete | None = None,
        create_link: bool = True,
    ) -> None: ...
    @property
    def entity_type_name(self): ...
