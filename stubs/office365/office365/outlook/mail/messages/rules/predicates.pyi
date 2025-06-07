from _typeshed import Incomplete
from office365.outlook.mail.recipient import Recipient as Recipient
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.types.collections import StringCollection as StringCollection

class MessageRulePredicates(ClientValue):
    bodyContains: Incomplete
    bodyOrSubjectContains: Incomplete
    categories: Incomplete
    fromAddresses: Incomplete
    hasAttachments: Incomplete
    headerContains: Incomplete
    importance: Incomplete
    isApprovalRequest: Incomplete
    def __init__(
        self,
        body_contains: Incomplete | None = None,
        body_or_subject_contains: Incomplete | None = None,
        categories: Incomplete | None = None,
        from_addresses: Incomplete | None = None,
        has_attachments: Incomplete | None = None,
        header_contains: Incomplete | None = None,
        importance: Incomplete | None = None,
        is_approval_request: Incomplete | None = None,
    ) -> None: ...
