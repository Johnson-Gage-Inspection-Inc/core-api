from _typeshed import Incomplete
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.gtp.base_request_options import BaseGptRequestOptions as BaseGptRequestOptions
from office365.sharepoint.gtp.message_entry import MessageEntry as MessageEntry

class ChatGptRequestOptions(BaseGptRequestOptions):
    Messages: Incomplete
    def __init__(self, messages: Incomplete | None = None) -> None: ...
