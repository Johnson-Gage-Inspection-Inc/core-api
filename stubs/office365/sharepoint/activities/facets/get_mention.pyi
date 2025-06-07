from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.activities.identity import ActivityIdentity as ActivityIdentity

class GetMentionFacet(ClientValue):
    mentionees: Incomplete
    def __init__(self, mentionees: Incomplete | None = None) -> None: ...
