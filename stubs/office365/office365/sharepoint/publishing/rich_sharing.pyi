from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.entity import Entity as Entity

class RichSharing(Entity):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def share_page_by_email(
        self, url, message, recipient_emails, page_content, subject
    ): ...
    def share_site_by_email(
        self, custom_description, custom_title, message, url, recipient_emails
    ): ...
    @property
    def entity_type_name(self): ...
