from _typeshed import Incomplete
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.translation.status import (
    TranslationStatus as TranslationStatus,
)
from office365.sharepoint.translation.status_set_request import (
    TranslationStatusSetRequest as TranslationStatusSetRequest,
)

class TranslationStatusCollection(Entity):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def set(self): ...
    def update_translation_languages(self): ...
    @property
    def untranslated_languages(self): ...
    @property
    def items(self): ...
