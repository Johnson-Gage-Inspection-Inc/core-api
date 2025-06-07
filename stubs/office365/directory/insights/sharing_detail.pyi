from _typeshed import Incomplete
from office365.directory.insights.identity import InsightIdentity as InsightIdentity
from office365.directory.insights.resource_reference import ResourceReference as ResourceReference
from office365.runtime.client_value import ClientValue as ClientValue

class SharingDetail(ClientValue):
    sharedBy: Incomplete
    sharedDateTime: Incomplete
    sharingReference: Incomplete
    sharingSubject: Incomplete
    sharingType: Incomplete
    def __init__(self, sharedBy=..., shared_datetime: Incomplete | None = None, sharing_reference=..., sharing_subject: Incomplete | None = None, sharing_type: Incomplete | None = None) -> None: ...
