from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.portal.userprofiles.sharedwithme.document_user import (
    SharedWithMeDocumentUser as SharedWithMeDocumentUser,
)

class SharedWithMeDocument(Entity):
    @property
    def authors(self) -> ClientValueCollection[SharedWithMeDocumentUser]: ...
    @property
    def caller_stack(self) -> str | None: ...
    @property
    def content_type_id(self) -> str | None: ...
    @property
    def doc_id(self) -> str | None: ...
    @property
    def editors(self): ...
    @property
    def modified(self): ...
    @property
    def file_leaf_ref(self) -> str | None: ...
    @property
    def entity_type_name(self): ...
