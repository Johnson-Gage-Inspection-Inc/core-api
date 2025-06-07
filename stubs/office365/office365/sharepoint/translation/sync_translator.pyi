from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.translation.item_info import (
    TranslationItemInfo as TranslationItemInfo,
)

class SyncTranslator(Entity):
    def __init__(self, context, target_language) -> None: ...
    def translate(self, input_file, output_file): ...
    @property
    def output_save_behavior(self) -> int | None: ...
    @property
    def entity_type_name(self): ...
