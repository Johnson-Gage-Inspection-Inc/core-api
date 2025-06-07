from _typeshed import Incomplete
from office365.onedrive.contenttypes.info import ContentTypeInfo as ContentTypeInfo
from office365.onedrive.documentsets.content import DocumentSetContent as DocumentSetContent
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class DocumentSet(ClientValue):
    welcomePageUrl: Incomplete
    allowedContentTypes: Incomplete
    defaultContents: Incomplete
    propagateWelcomePageChanges: Incomplete
    shouldPrefixNameToFile: Incomplete
    def __init__(self, welcome_page_url: Incomplete | None = None, allowed_content_types: Incomplete | None = None, default_contents: Incomplete | None = None, propagate_welcome_page_changes: Incomplete | None = None, should_prefix_name_to_file: Incomplete | None = None) -> None: ...
