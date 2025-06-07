from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ComplianceTag(ClientValue):
    AcceptMessagesOnlyFromSendersOrMembers: Incomplete
    AccessType: Incomplete
    def __init__(self, accept_messages_only_from_senders_or_members: Incomplete | None = None, access_type: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...
