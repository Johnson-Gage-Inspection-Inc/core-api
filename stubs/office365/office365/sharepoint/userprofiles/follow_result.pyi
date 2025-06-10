from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.userprofiles.followed_item import FollowedItem as FollowedItem

class FollowResult(ClientValue):
    Item: Incomplete
    ResultType: Incomplete
    def __init__(self, item=..., result_type: Incomplete | None = None) -> None: ...
